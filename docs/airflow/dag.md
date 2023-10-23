---
tags:
  - DAG
  - BashOperator
  - PythonOperator
icon: simple/apacheairflow
---
# Creating Airflow DAGs

## Introduction

In this tutorial, we will learn how to create and manage Directed Acyclic Graphs (DAGs) in Apache Airflow. Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. DAGs in Airflow represent a collection of tasks with defined dependencies, allowing you to build and schedule complex data pipelines.

## Prerequisites

Before we begin, make sure you have the airflow service up and running via docker.

## Instructions

### Step 1: Project Setup

First, set up a project directory to organize your Airflow DAGs and scripts. Here's a recommended project structure:

```plaintext
project_root/
│
├── dags/
│   └── your_dag.py
│
├── scripts/
│   └── your_script.py
│
└── ...
```

### Step 2: Create a DAG

A DAG is a Python script that defines the structure of your workflow. Create a python file under the dag directory with the name `sandbx.py`

Here's a basic example of how to create a simple DAG:

### Step 3: Importing Required Modules

In the first step of creating an Apache Airflow DAG, you need to import the necessary modules and libraries to build your workflow. These modules provide the tools and components required for defining and executing tasks within the DAG.

```python title="sandbox.py"
import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
```

The first step in writing a DAG (Directed Acyclic Graph) file for Apache Airflow involves creating a DAG object. In your provided code snippet, you've initiated a DAG named "sandbox" with various attributes and configurations. 

```python title="sandbox.py"
dag = DAG(
    dag_id="sandbox",
    schedule="0 0 * * *",   # https://crontab.guru/
    start_date=days_ago(0),
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=["labs", "damg7245"],
    # params=user_input,
)
```

Let's break down the code and explain each part:

* **dag_id**: This is a unique identifier for your DAG. In this case, it's named "sandbox," but you should use a meaningful and descriptive name for your specific use case.
* **schedule**: This attribute defines the schedule or frequency at which the DAG should run. In your example, the schedule is set to "0 0 * * *," which corresponds to a daily schedule at midnight. The format follows a cron-like pattern. You can use tools like crontab.guru to help generate the desired cron expression for your specific schedule requirements.
* **start_date**: This attribute sets the initial date when your DAG should start running. In your code, days_ago(0) is used to specify the current date and time as the start date.
* **catchup**: When set to False, as in your code, it means that the DAG won't "catch up" on any missed runs if the schedule's start date is in the past. If set to True, Airflow will execute runs for any missed intervals.
* **dagrun_timeout**: This attribute defines the maximum amount of time allowed for a DAG run to execute. In your code, it's set to a timeout of 60 minutes. If a DAG run exceeds this duration, it will be * **marked as failed.
* **tags**: Tags are labels or metadata that you can associate with your DAG. In your code, you've added two tags, "labs" and "damg7245." Tags can be useful for categorizing and organizing your DAGs.
* **params**: This is commented out in your code but can be used to pass parameters to your DAG. If you have specific parameters or configurations that your DAG needs, you can provide them here.

### Step 4: Task Using BashOperator 

This task is implemented using a `BashOperator`, which allows you to execute a shell command as part of your workflow. 

```python title="sandbox.py"
with dag:
    hello_world = BashOperator(
        task_id="hello_world",
        bash_command='echo "Hello from airflow"'
    )
```

Here's what this specific task does:

This command uses the echo command to output the text "Hello from Airflow" to the standard output (usually the terminal). In Airflow, this text will be logged and can be viewed in Airflow's logs or user interface.

### Step 5: Task Using PythonOperator 

This task is implemented using a `BashOperator`, which allows you to execute a python command as part of your workflow. 

```python title="sandbox.py"

def print_keys(**kwargs):
    print("-----------------------------")
    print(f"Your Secret key is: {os.getenv('OPENAI_KEY')}") # Donot print this anywhere, this is just for demo
    print("-----------------------------")

    .
    .
    .

    fetch_keys = PythonOperator(
        task_id='fetch_keys',
        python_callable=print_keys,
        provide_context=True,
        dag=dag,
    )
```
Here's what this specific task does:

It prints the value of the environment variable OPENAI_KEY by using os.getenv('OPENAI_KEY'). This is intended to show the value of a secret key, but a comment indicates that it should not be printed anywhere, as it is sensitive information.

???+ warning
    Never print sensitive variables into logs

### Step 6: Task Dependency


```python title="sandbox.py"
    # Flow
    hello_world >> fetch_keys >> bye_world
```

The `hello_world`, `fetch_keys`, and `bye_world` tasks are linked together to form a workflow. The `>>` operator signifies task dependencies, meaning that fetch_keys should only execute if hello_world completes successfully, and bye_world should only execute after fetch_keys has successfully finished. This creates a sequential flow for your tasks.

### Step 7: Execute the DAG


To execute the DAG, locate and click the "Trigger DAG" button. This will initiate a new run of the DAG. You can monitor the progress of the DAG run by navigating to the "DAG Runs" tab, where you can view the status of the most recent and historical runs. Logs and status updates will be available in real-time. To inspect the logs and outputs of specific tasks within the DAG, you can click on individual task instances within the "DAG Runs" tab.

## Conclusion
In this tutorial, we've learned how to create and manage Airflow DAGs. You can now build complex workflows by adding more tasks and defining their dependencies. Airflow provides a powerful way to automate and monitor data pipelines.