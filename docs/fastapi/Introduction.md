---
tags:
  - FastAPI
icon: simple/fastapi
---
# FastAPI 

## Introduction

[**FastAPI**](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It's designed to be easy to use and provide high-performance, while also offering automatic, interactive documentation. This tutorial will guide you through the basics of FastAPI, so you can start building your web applications and APIs with ease.

## Why FastAPI?

FastAPI is gaining popularity rapidly, and here's why:

- **Fast**: It's one of the fastest web frameworks available for Python, thanks to its asynchronous support.
- **Easy to Use**: FastAPI leverages Python type hints to simplify API development and reduce the need for boilerplate code.
- **Automatic Documentation**: It generates interactive API documentation using OpenAPI and JSON Schema.
- **Data Validation**: It offers built-in data validation using Pydantic, helping to keep your data clean and reliable.
- **Asynchronous Support**: FastAPI supports asynchronous programming, which is particularly useful for handling I/O-bound operations efficiently.
- **Scalable**: It's designed for both small projects and large, high-traffic applications.
- **Testable**: It has excellent support for testing, making it easy to verify the correctness of your APIs.

In this tutorial, you'll get started with FastAPI, create your first FastAPI application, understand routing, handle requests, and explore the fundamentals of building APIs with this powerful framework.

Before we dive into the code, make sure you have Python 3.7 or higher installed and are ready to begin your journey with FastAPI.

Let's get started!

## Installation and Setup

Before we dive into building FastAPI applications, let's make sure you have FastAPI and its dependencies installed. We'll also create a virtual environment to keep your project dependencies isolated.

### Step 1: Prerequisites

Before proceeding, ensure you have the following prerequisites in place:

- Python: Streamlit is a Python library, so you'll need Python installed. If you haven't already, you can [download Python here](https://www.python.org/downloads/). Recommended version 3.x+

### Step 2: Create a Virtual Environment

It's a good practice to create a virtual environment for your FastAPI project to manage dependencies cleanly. In this tutorial, we'll use pipenv to create and manage the virtual environment.

```bash
pipenv shell
```

You'll notice your terminal prompt changes, indicating that you are now inside the virtual environment. Any packages you install or scripts you run will be isolated within this environment.

### Step 3: Install Production Dependencies

FastAPI, Pandas, Gunicorn, and Uvicorn, along with their required dependencies, will be installed in your virtual environment. These dependencies are suitable for production use.

```shell
pipenv install fastapi pandas gunicorn uvicorn
```

### Step 4: Install Development Dependencies

For development and testing, you can install additional dependencies. Run the following command to install development dependencies:

```shell
pipenv install pytest-cov httpx
```
These dependencies include pytest-cov for testing coverage and httpx for making HTTP requests during development.

### Step 5: Create a New Python File

Start by creating a new Python file in your preferred code editor or IDE. Name it, for example, `main.py`.


### Step 6: Import FastAPI

Inside your `main.py` file, import FastAPI by adding the following line at the top:

```python
import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
```

### Step 7: Create an Instance of FastAPI
Now, create an instance of the FastAPI class to represent your web application. Add the following line to your main.py file:

```python
app = FastAPI()
```

### Step 8: Define a Route and Endpoint
Let's define a route and an endpoint. In FastAPI, you use Python functions as endpoints. Create a "Hello World" endpoint that returns a JSON response:

```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

* `@app.get("/")` is a decorator that specifies the HTTP method (GET) and the URL path ("/") that this endpoint will respond to.

* def read_root(): is a Python function that will be executed when someone accesses the root path ("/").

* return `{"message": "Hello World"}` returns a JSON response with a simple greeting.

### Step 9: Run Your Application

To run your FastAPI application, use Uvicorn. Open your terminal, navigate to the directory containing your main.py file, and run the following command:

```python
uvicorn main:app --reload
```

* `main:app` specifies the Python file (`main.py`) and the FastAPI app instance (`app`) to run

* `--reload` enables auto-reloading, which is useful during development.


### Step 10: Access Your Application

Once the application is running, open your web browser or API client and access your FastAPI application. You should see the "Hello World" message displayed as a JSON response.

Congratulations! You've successfully created your first FastAPI application, following each step. This simple example demonstrates the basics of routing and handling requests with FastAPI. You can build on this foundation to create more complex and feature-rich APIs.


## Understanding the FastAPI Application

In this section, we'll break down the structure of the FastAPI application code you've provided and explain the purpose of each component. This will give you a clearer understanding of how FastAPI works.


```python title="main.py"
# Import necessary modules and packages
import uvicorn  # To run the FastAPI application
import pandas as pd  # For data handling
from fastapi import FastAPI  # FastAPI framework
from pydantic import BaseModel  # For defining request body models
from fastapi.responses import JSONResponse  # For returning JSON responses

# Create a FastAPI instance
app = FastAPI()

# Define a Pydantic model to validate user input
class UserInput(BaseModel):
    state: str  # Define the input field 'state' as a string

# Function to load data from a remote source
def load_df():
    # Define column specifications to parse a fixed-width file
    cols = [
        (20, 51),    # Name
        (72, 75),    # ST
        (106, 116),  # Lat
        (116, 127)   # Lon
    ]
    
    # Read data from the provided URL and apply column specifications
    df = pd.read_fwf("https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt", colspecs=cols, skiprows=[1])
    
    # Filter out rows where the 'ST' column is not NaN (not missing)
    df = df[df['ST'].notna()]
    return df

# Define a route for a health check endpoint
@app.get("/api/v1/healthcheck")
async def say_hello() -> dict:
    return {"message": "Ok"}  # Return a JSON response indicating that the service is healthy

# Define a default route for the root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"}  # Return a simple "Hello World" message as a JSON response

# Define a route to fetch all data
@app.get("/api/v1/fetch_all_data")
def fetch_data() -> JSONResponse:
    # Load data using the load_df function
    df = load_df()
    return JSONResponse(content=df.to_dict(orient='records'))  # Return the data as a JSON response

# Define a route to fetch data filtered by a specific state
@app.post("/api/v1/fetch_by_state")
def fetch_data(userinput: UserInput) -> JSONResponse:
    # Load data using the load_df function
    df = load_df()
    
    # Filter the data based on the user's specified state (converted to uppercase)
    filtered_df = df[df['ST'] == userinput.state.upper()]
    
    return JSONResponse(content=filtered_df.to_dict(orient='records'))  # Return the filtered data as a JSON response

```

## Additional Resources

In your journey to mastering FastAPI, you may find the following resources valuable for further learning and exploration:

### Official FastAPI Documentation
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/): The official documentation is an invaluable resource for understanding every aspect of FastAPI, including detailed explanations, tutorials, and advanced features.

### FastAPI GitHub Repository
- [FastAPI GitHub Repository](https://github.com/tiangolo/fastapi): Explore the source code, report issues, and contribute to the development of FastAPI on GitHub.

### FastAPI User Guide
- [FastAPI User Guide](https://fastapi.tiangolo.com/tutorial/first-steps/): This section of the documentation provides practical guidance on using FastAPI for various tasks and use cases.

These resources offer a wealth of information, tutorials, and community support to help you enhance your FastAPI skills and build powerful web applications and APIs. Don't hesitate to explore them and continue your journey of learning and building with FastAPI.

