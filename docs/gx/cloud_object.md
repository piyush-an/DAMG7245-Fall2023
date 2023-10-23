---
date: 2023-10-22
tags:
  - GX
  - AWS
  - S3
readtime: 15
icon: simple/amazons3
---
## AWS S3 Object Storage (CSV Files)

In this section, we will explore using Great Expectations to validate data stored in AWS S3, a popular object storage service provided by Amazon Web Services.

In our accompanying Jupyter Notebook, you'll find detailed code examples and step-by-step instructions for each of these tasks. Let's start using Great Expectations to validate data stored in AWS S3 object storage!

!!! Notebook 
    Refer this notebook [notebooks/gx/gx_sql_db.ipynb](https://github.com/piyush-an/DAMG7245-Fall2023/blob/main/notebooks/gx/gx_s3.ipynb)

## Notebook Overview

### Initializing the Great Expectations Directory

To begin, you'll need to initialize a Great Expectations directory for your project. This directory will store your data validation configurations, expectations, and checkpoints. You can use the "init" command to set up the directory structure. Detailed code for this initialization can be found in our accompanying Jupyter Notebook.

### Creating a Data Source for AWS S3

Great Expectations allows you to create data sources that connect to your data stored in different locations. In this case, we will create a data source connecting to AWS S3. You will need to specify the name of the data source, the S3 bucket name where your data is stored, and other connection details. We will provide code examples in the notebook for creating this S3 data source, which will be named "S3_NYC_Yellow_Taxi2."

### Creating an Expectations Suite

With the S3 data source set up, you can proceed to define expectations for your data. Expectations help you specify what you anticipate in your data, such as data types, value constraints, and other properties. The Jupyter Notebook contains code examples to guide you through creating an expectations suite for your S3-stored data.

### Creating a Checkpoint

Checkpoints are crucial for monitoring your data quality over time. They capture the state of your data at specific points and help you track its quality. We will demonstrate how to create a checkpoint to monitor your S3 data against your defined expectations using Great Expectations.

### Viewing the Data Report

Great Expectations generates Data Docs that provide comprehensive reports on your data. These reports include data profiling, data validation results, and other valuable information. You can use Data Docs to gain insights into your data's quality and potential issues. We will show you how to view these reports in the notebook.

