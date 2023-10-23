---
tags:
  - FastAPI
  - pytest
icon: simple/pytest
---

# Unit Testing with Pytest

Unit testing is a crucial aspect of software development. In this section, you'll learn how to write unit tests for your FastAPI application using the Pytest testing framework. We'll use the `TestClient` provided by FastAPI to send HTTP requests to your application and verify the expected responses.

## Prerequisites

Before getting started with unit testing, ensure that you have `Pytest` and `httpx` installed. You can install it using pipenv:

## Instructions

### Step 1: Setting up TestClient

To begin unit testing, set up the TestClient for your FastAPI application. The TestClient is a convenient tool for sending HTTP requests and receiving responses within your tests. Here's an example of how to set it up:

```python
# test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
```

Make sure to import the TestClient and your FastAPI application (app) from your main application file.

### Step 2: Writing Unit Tests

Now, let's write some unit tests for your FastAPI application. We'll provide a few examples to get you started.

#### Test the Health Check Endpoint

The following test checks the health check endpoint:

```python
def test_healthcheck():
    response = client.get(
        url="/api/v1/healthcheck"
    )
    assert response.status_code == 200
    message = response.json()["message"]
    assert message == "Ok"
```

This test sends a GET request to the `/api/v1/healthcheck` endpoint and verifies that the response status code is `200` (indicating success) and that the response message is `"Ok"`

#### Test the fetch_all_data Endpoint
You can test an endpoint that fetches all data:
```python
def test_fetch_all_data():
    response = client.get(
        url="/api/v1/fetch_all_data"
    )
    assert response.status_code == 200
    assert len(response.json()) == 205
```

This test sends a GET request to the `/api/v1/fetch_all_data` endpoint and checks that the response status code is `200`. It also verifies that the response contains `205` items (modify this number based on your data).


#### Test the fetch_by_state Endpoint
You can write tests for an endpoint that fetches data by state:
```python
def test_fetch_by_state_ma():
    response = client.post(
        url="/api/v1/fetch_by_state",
        json={
            "state": "ma"
        }
    )
    assert response.status_code == 200
    assert len(response.json()) == 2
```
This test sends a POST request to the `/api/v1/fetch_by_state` endpoint with a JSON payload. It checks that the response status code is `200` and that the response contains `2` items. You can write similar tests for different states.

### Step 3: Running the Tests

You can run your tests using the following command:

```bash
pytest test_main.py
```

Test Report with Code coverage report

```plaintext title="stdout"
============================= test session starts ==============================
platform linux -- Python 3.12.0, pytest-7.4.2, pluggy-1.3.0 -- /home/runner/.local/share/virtualenvs/fastapi-ujMFs4rz/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/DAMG7245-Fall2023/DAMG7245-Fall2023/fastapi
plugins: anyio-3.7.1, cov-4.1.0
collecting ... collected 5 items

test_main.py::test_healthcheck PASSED                                    [ 20%]
test_main.py::test_fetch_all_data PASSED                                 [ 40%]
test_main.py::test_fetch_by_state_ma PASSED                              [ 60%]
test_main.py::test_fetch_by_state_MA PASSED                              [ 80%]
test_main.py::test_fetch_by_state_MAA PASSED                             [100%]

=============================== warnings summary ===============================
../../../../.local/share/virtualenvs/fastapi-ujMFs4rz/lib/python3.12/site-packages/dateutil/tz/tz.py:37
  /home/runner/.local/share/virtualenvs/fastapi-ujMFs4rz/lib/python3.12/site-packages/dateutil/tz/tz.py:37: DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).
    EPOCH = datetime.datetime.utcfromtimestamp(0)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================= 5 passed, 1 warning in 5.96s =========================
Name           Stmts   Miss  Cover   Missing
--------------------------------------------
main.py           28      1    96%   29
test_main.py      24      0   100%
--------------------------------------------
TOTAL             52      1    98%
```

## Conclusion
Writing unit tests for your FastAPI application is crucial for ensuring the correctness of your endpoints and data. These tests help identify issues early in the development process and provide confidence in the reliability of your API.

## Further Reading

- [Pytest Official Documentation](https://docs.pytest.org/en/latest/): The official documentation is an excellent resource for getting started with Pytest and mastering its features.

- [Effective Pytest by Martin Thoma](https://martin-thoma.com/testing-python-code/): This guide provides practical tips and best practices for writing effective Pytest tests.
