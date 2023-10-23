---
tags:
  - GX
  - PostgreSQL
icon: simple/postgresql
---
## PostgreSQL Data Source

In this section, we will explore using Great Expectations with a PostgreSQL data source. We'll be running PostgreSQL in a Docker container locally for demonstration purposes.


In our accompanying Jupyter Notebook, you'll find detailed code examples and step-by-step instructions for each of these tasks. Let's start using Great Expectations to validate data in your locally running PostgreSQL database!

!!! Notebook 
    Refer this notebook [notebooks/gx/gx_sql_db.ipynb](https://github.com/piyush-an/DAMG7245-Fall2023/blob/main/notebooks/gx/gx_sql_db.ipynb)

## Notebook Overview

### Initializing the Great Expectations Directory

Before diving into data validation, you'll need to initialize a Great Expectations directory for your project. This directory will store your data validation configurations, expectations, and checkpoints. You can use the "init" command to set up the directory structure. The detailed code for this can be found in our accompanying Jupyter Notebook.


### Inserting Data into the Database Table

To work with data in the PostgreSQL database, you'll need some sample data. We will insert data into a database table from an external source, in this case, the NOAA weather stations dataset. The data will be fetched from [this URL](https://www.ncei.noaa.gov/access/homr/file/nexrad-stations.txt). You will find the code for this data insertion in our notebook.

### Creating a Data Source

After initializing the Great Expectations directory and loading data into your PostgreSQL database, the next step is to create a data source. This involves specifying the database connection details and the table you want to validate. The Jupyter Notebook contains code examples for creating a data source.

### Creating an Expectations Suite

Once you have your data source set up, you can start defining expectations for your data. Expectations help you specify what you anticipate in your data, such as data types, value constraints, and other properties. We will provide code examples in the notebook to guide you through creating an expectations suite.

### Creating a Checkpoint

Checkpoints are essential for monitoring your data over time. They capture the state of your data at specific moments and help you track its quality. We will demonstrate how to create a checkpoint to monitor your PostgreSQL data against your expectations using Great Expectations.

### Viewing the Data Report

Great Expectations generates Data Docs that offer detailed reports on your data. These reports include data profiling, data validation results, and other valuable information. You can use Data Docs to get insights into your data's quality and any potential issues. We'll show you how to view these reports in the notebook.
