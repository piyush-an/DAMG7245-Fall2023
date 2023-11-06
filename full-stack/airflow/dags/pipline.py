from __future__ import annotations

from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param
from airflow.utils.task_group import TaskGroup

import os
import pendulum
from pprint import pprint


user_input = {
    "datasource_url": Param(default="https://raw.githubusercontent.com/bsbodden/redis_vss_getting_started/main/data/bikes.json", type='string', minLength=5, maxLength=255),
}

with DAG(
    dag_id="data_load_pipeline",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["DAMG725", "demo"],
    params=user_input,
) as dag:
    
    # Dummy Task
    @task(task_id="print_the_context")
    def print_context(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        print("-----------------------------")
        pprint(kwargs)
        print("-----------------------------")
        print(ds)
        print("-----------------------------")
        return "Whatever you return gets printed in the logs"

    with TaskGroup(group_id="stage1-fetch_data") as stage_1:
        @task(task_id="fetch_data")
        def fetch_data(ds=None, **kwargs):
            """Fetch data from a url"""
            import requests
            response = requests.get(kwargs["params"]["datasource_url"])
            bikes = response.json()
            kwargs["ti"].xcom_push(key="bikes", value=bikes)
            return 

        fetch_data()
    
    with TaskGroup(group_id="stage2-redis_db_reset") as stage_2:
        @task(task_id="handshake_redis")
        def handshake(ds=None, **kwargs):
            import redis
            client = redis.Redis(host=os.getenv("REDIS_HOST", "redis-stack"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
            res = client.ping()
            assert res == True
            client.close()
        
        @task(task_id="database_cleanup")
        def database_cleanup(ds=None, **kwargs):
            import redis
            client = redis.Redis(host=os.getenv("REDIS_HOST", "redis-stack"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
            client.flushdb()
            client.close()

        handshake() >> database_cleanup()

    with TaskGroup(group_id="stage3-load_data_into_redis") as stage_3:
        
        @task(task_id="load_raw_data")
        def load_raw_data(ds=None, **kwargs):
            import redis
            client = redis.Redis(host=os.getenv("REDIS_HOST", "redis-stack"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
            pipeline = client.pipeline()
            bikes = kwargs["ti"].xcom_pull(key="bikes", task_ids="stage1-fetch_data.fetch_data")
            for i, bike in enumerate(bikes, start=1):
                redis_key = f"bikes:{i:03}"
                pipeline.json().set(redis_key, "$", bike)
            res = pipeline.execute()
            client.close()
            print(res)
        
        @task(task_id="append_embedding_data")
        def load_embedding(ds=None, **kwargs):
            import redis
            client = redis.Redis(host=os.getenv("REDIS_HOST", "redis-stack"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
            keys = sorted(client.keys("bikes:*"))
            import numpy as np
            from sentence_transformers import SentenceTransformer
            embedder = SentenceTransformer('msmarco-distilbert-base-v4')
            descriptions = client.json().mget(keys, "$.description")
            descriptions = [item for sublist in descriptions for item in sublist]
            embeddings = embedder.encode(descriptions).astype(np.float32).tolist()
            VECTOR_DIMENSION = len(embeddings[0])
            kwargs["ti"].xcom_push(key="VECTOR_DIMENSION", value=VECTOR_DIMENSION)
            assert VECTOR_DIMENSION == 768
            pipeline = client.pipeline()
            for key, embedding in zip(keys, embeddings):
                pipeline.json().set(key, "$.description_embeddings", embedding)
            pipeline.execute()
            client.close()

        @task(task_id="create_indexes")
        def create_indexes(ds=None, **kwargs):
            import redis
            from redis.commands.search.field import (
                NumericField,
                TagField,
                TextField,
                VectorField,
            )
            from redis.commands.search.indexDefinition import IndexDefinition, IndexType
            VECTOR_DIMENSION = kwargs["ti"].xcom_pull(key="VECTOR_DIMENSION", task_ids="stage3-load_data_into_redis.append_embedding_data")
            client = redis.Redis(host=os.getenv("REDIS_HOST", "redis-stack"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
            schema = (
                TextField("$.model", no_stem=True, as_name="model"),
                TextField("$.brand", no_stem=True, as_name="brand"),
                NumericField("$.price", as_name="price"),
                TagField("$.type", as_name="type"),
                TextField("$.description", as_name="description"),
                VectorField(
                    "$.description_embeddings",
                    "FLAT",
                    {
                        "TYPE": "FLOAT32",
                        "DIM": VECTOR_DIMENSION,
                        "DISTANCE_METRIC": "COSINE",
                    },
                    as_name="vector",
                ),
            )
            definition = IndexDefinition(prefix=["bikes:"], index_type=IndexType.JSON)
            res = client.ft("idx:bikes_vss").create_index(
                fields=schema, definition=definition
            )
            assert res == "OK"
            client.close()

        load_raw_data() >> load_embedding() >> create_indexes()

    print_context() >> stage_1 >> stage_2 >> stage_3