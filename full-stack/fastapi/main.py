import os
import time
import json
import pandas as pd
import numpy as np
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import redis
from redis.commands.search.query import Query

app = FastAPI()

# Middleware to add process time header
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Redis connection
client = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=os.getenv("REDIS_PORT", 6379), decode_responses=True)
index_name = "idx:bikes_vss"

# Embedding model
from sentence_transformers import SentenceTransformer
embedder = SentenceTransformer('msmarco-distilbert-base-v4')

# Pydantic models
class UserBrandInput(BaseModel):
    brand_name:str

class UserQueryInput(BaseModel):
    queries:list

@app.get("/api/v1/redishealthcheck", tags=["Healthcheck"])
async def say_hello() -> dict:
    res = client.ping()
    result = {"message": res}
    return JSONResponse(content=result)


@app.get("/api/v1/healthcheck", tags=["Healthcheck"])
async def say_hello() -> dict:
    result = {"message":"Ok"}
    return JSONResponse(content=result)

@app.get("/")
async def root():
    result = {"message": "Hello User"}
    return JSONResponse(content=result)

@app.get("/api/v1/fetch_brands", tags=["Query"])
async def fetch_data() -> JSONResponse:
    """fetches all the unique brands from the dataset"""
    # check if the result is cached
    cache = client.get("unique_brands")
    if cache:
        print("cache hit")
        # return the cached result
        result = {"brands": json.loads(cache)}
        return JSONResponse(content=result)
    else:
        print("cache miss")
        query = Query("*").return_fields("brand")
        res = client.ft("idx:bikes_vss").search(query).docs
        unique_brands = set()
        for doc in res:
            unique_brands.add(doc["brand"])
        # cache the result for 30 seconds
        client.set("unique_brands", json.dumps(list(unique_brands)))
        client.expire("unique_brands", 30)
        result = {"brands": list(unique_brands)}
        return JSONResponse(content=result)

@app.post("/api/v1/filter_by_brand", tags=["Query"])
async def fetch_data(userinput: UserBrandInput) -> JSONResponse:
    """filters the dataset by brand"""
    query = Query(f"@brand:{userinput.brand_name}").return_fields("model", "brand", "price", "type")
    res = client.ft("idx:bikes_vss").search(query).docs
    parsed_data = []
    for document in res:
        document_dict = {
            "id": document.id,
            "payload": document.payload,
            "model": document.model,
            "brand": document.brand,
            "price": document.price,
            "type": document.type
        }
        parsed_data.append(document_dict)
    df = pd.DataFrame(parsed_data)
    return JSONResponse(df.to_dict(orient="records"))


@app.post("/api/v1/similar", tags=["Query"])
async def fetch_data(userinput: UserQueryInput) -> JSONResponse:
    """fetches similar bikes based on user input"""
    encoded_queries = embedder.encode(userinput.queries)
    query = (
        Query("(*)=>[KNN 3 @vector $query_vector AS vector_score]")
        .sort_by("vector_score")
        .return_fields("vector_score", "id", "brand", "model", "description")
        .dialect(2)
    )
    res = create_query_table(query, userinput.queries, encoded_queries)
    df = pd.DataFrame(res)
    return JSONResponse(df.to_dict(orient="records"))


def create_query_table(query, queries, encoded_queries, extra_params={}):
    results_list = []
    for i, encoded_query in enumerate(encoded_queries):
        result_docs = (
            client.ft("idx:bikes_vss")
            .search(
                query,
                {
                    "query_vector": np.array(
                        encoded_query, dtype=np.float32
                    ).tobytes()
                }
                | extra_params,
            )
            .docs
        )
        for doc in result_docs:
            vector_score = round(1 - float(doc.vector_score), 2)
            results_list.append(
                {
                    "query": queries[i],
                    "score": vector_score,
                    "id": doc.id,
                    "brand": doc.brand,
                    "model": doc.model,
                    "description": doc.description,
                }
            )
        return results_list

# def main():
#     uvicorn.run(app, host="0.0.0.0", port=80, reload=True)

# if __name__ == "__main__":
#     main()
