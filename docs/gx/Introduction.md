---
tags:
  - GX
---

# Great Expectations

## Introduction

[**Great Expectations**](https://greatexpectations.io/) is an open-source Python library that plays a crucial role in the realm of data validation and testing for data pipelines and data quality assurance. In a data-driven world, the reliability and trustworthiness of data are paramount, and Great Expectations helps data professionals, data engineers, and data scientists ensure that their data meets expectations and maintains quality.

## Key Concepts

- **Data Validation**: Great Expectations provides a framework for setting, documenting, and validating data expectations. It allows you to define the rules and criteria your data must adhere to, ensuring that it remains consistent and reliable.

- **Data Quality**: With Great Expectations, you can monitor and improve the quality of your data. By setting and continuously validating expectations, you can catch issues early, preventing bad data from propagating through your systems.

- **Automated Testing**: Great Expectations can be integrated into automated testing pipelines, providing confidence in the data's integrity as it moves through different stages of your data architecture.

In this tutorial, we will explore the core concepts and practical usage of Great Expectations, including setting expectations, validating data, and advanced features like data profiling and automated testing. Let's get started!

## Prerequisites

Before we dive into Great Expectations, make sure you have the following prerequisites in place:

- **Python**: You should have Python installed on your system. If you don't have it installed, you can download it from the official [Python website](https://www.python.org/downloads/).

- **Python Environment**: It's a good practice to create a virtual environment for your Great Expectations project. You can use Python's built-in `venv` module or a third-party tool like `conda` or `virtualenv` to create an isolated environment.

- **Great Expectations Installation**: You'll need to install Great Expectations to use it. If you haven't already, you can install it using `pip` by running:

    ```bash
    pip install great-expectations
    ```

- **Data Source**: To follow along with the tutorial effectively, you should have access to a dataset or data source that you want to validate and test using Great Expectations.

Now that you've checked off these prerequisites, you're ready to start setting up and working with Great Expectations.

## Data Sources for Great Expectations (gx)

In this tutorial, we will explore three different data sources for working with Great Expectations (gx), each offering unique ways to validate and test your data:

### 1. Local File System (CSV Files)

- The local file system serves as a common and convenient data source for many data validation tasks.
- You can validate data stored in CSV files, making it suitable for scenarios where your data is stored locally.

### 2. PostgreSQL Database

- PostgreSQL is a powerful relational database system that allows you to manage, query, and analyze your data.
- We will demonstrate how to connect Great Expectations to a PostgreSQL database to set expectations and validate data stored in database tables.

### 3. AWS S3 Object Storage

- Amazon S3 (Simple Storage Service) is a cloud-based object storage service provided by Amazon Web Services.
- You can use Great Expectations to connect to an AWS S3 bucket to validate data stored in cloud-based object storage.

Each of these data sources has its own unique set of requirements and considerations, and we'll walk you through how to work with them using Great Expectations.

