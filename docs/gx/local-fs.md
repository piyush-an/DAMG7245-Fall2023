---
tags:
  - GX
# icon: file_folder
---
# Local File System (CSV Files)

In this section, we will focus on using Great Expectations with a local file system, specifically working with CSV files. This is a common use case when you have data stored locally and want to validate it using Great Expectations.

In our accompanying Jupyter Notebook, you will find detailed code examples and step-by-step instructions for each of these tasks. Let's get started with using Great Expectations to validate your local CSV data!

!!! Notebook 
    Refer this notebook [notebooks/gx/gx_local_csv.ipynb](https://github.com/piyush-an/DAMG7245-Fall2023/blob/main/notebooks/gx/gx_local_csv.ipynb)

## Notebook Overview

### Creating a Data Source

To get started, you'll need to create a data source that points to the location of your CSV files. This step involves defining the structure and properties of your data source, such as the file path and column names.
### Setting Expectations

Once you have defined your data source, the next step is to set expectations for your data. Expectations define the rules and criteria that your data must adhere to. You can specify expectations on data types, value ranges, uniqueness, and more. Our notebook provides code examples for setting expectations based on your specific data requirements.

### Creating a Checkpoint

Checkpoints in Great Expectations allow you to capture the state of your data at a particular point in time. You can think of checkpoints as snapshots of your data that help you track its quality and integrity over time. We will guide you through the process of creating a checkpoint to monitor your data against your defined expectations.

### Viewing the Data Report

Great Expectations generates Data Docs that provide comprehensive reports on your data. These reports include data profiling, data validation results, and other relevant information. We will demonstrate how to use Data Docs to view detailed reports on your data, making it easier to understand its quality and any issues that may need attention.

