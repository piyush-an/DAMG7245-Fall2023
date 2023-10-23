import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.param import Param
from datetime import timedelta

dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
    # params=user_input,
)

def print_keys(**kwargs):
    print("-----------------------------")
    print(f"Your Secret key is: {os.getenv('OPENAI_KEY')}") # Donot print this anywhere, this is just for demo
    print("-----------------------------")


with dag:
    hello_world = BashOperator(
        task_id="hello_world",
        bash_command='echo "Hello from airflow"'
    )

    fetch_keys = PythonOperator(
        task_id='fetch_keys',
        python_callable=print_keys,
        provide_context=True,
        dag=dag,
    )


    bye_world = BashOperator(
        task_id="bye_world",
        bash_command='echo "Bye from airflow"'
    )

    hello_world >> fetch_keys >>  bye_world

