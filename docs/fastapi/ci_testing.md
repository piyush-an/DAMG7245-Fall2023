---
tags:
  - FastAPI
  - pytest
  - GithubAction
icon: simple/githubactions
# links:
#   - container/build_fastapi.md
---

# Continuous Integration (CI) Testing with GitHub Actions

Continuous Integration (CI) is a software development practice that involves automatically testing and building your code every time changes are pushed to a version control repository. GitHub Actions is a powerful CI/CD (Continuous Integration/Continuous Deployment) platform provided by GitHub, and it can be used to automate the testing of your FastAPI application. In this section, we'll explore how to set up CI testing for your FastAPI project using GitHub Actions.

## Prerequisites

Before setting up CI testing with GitHub Actions, ensure you have the following:

1. A GitHub repository that contains your FastAPI project.

2. A working knowledge of GitHub and GitHub Actions.

## Creating a GitHub Actions Workflow

GitHub Actions workflows are defined in `.yaml` files within your repository. These workflows specify the series of steps to run when specific events occur. To set up CI testing, follow these steps:

### Step 1: Create a `.github/workflows` Directory

In your GitHub repository, create a `.github/workflows` directory if it doesn't already exist. This is where you'll store your GitHub Actions workflow files.

### Step 2: Create a Workflow YAML File

Inside the `.github/workflows` directory, create a new YAML file, such as `fastapi-ci.yml`, and define your CI testing workflow.

Here's a basic example of a CI testing workflow for a FastAPI project:

```yaml title="fastapi-ci.yml"
name: fastapi-ci  # Name your CI/CD workflow, e.g., "fastapi-ci"

on:
  push:
    paths:
      - 'fastapi/**'  # Trigger this workflow when changes are pushed to the 'fastapi/' directory
      # TODO: Change the path to match the directory you want to monitor for changes

jobs:
  unit-tests:
    runs-on: ubuntu-latest  # Use the latest version of the Ubuntu runner

    steps:
      - 
        name: Checkout  # Step to check out the code from the repository
        uses: actions/checkout@v3

      - 
        id: commit
        uses: pr-mpt/actions-commit-hash@v2  # Step to retrieve the commit hash

      - 
        name: Set up Python 3.12  # Step to set up Python 3.12 for testing
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'  # Specify the Python version you want to use
          # TODO: Change to your desired Python version

      - 
        name: Install pipenv  # Step to install the pipenv package manager
        run: pip install pipenv

      - 
        name: Run tests  # Step to run unit tests
        working-directory: ./fastapi  # Change to the directory where your tests are located
        run: |
          pipenv install --dev  # Install project dependencies and dev dependencies using pipenv
          pipenv run coverage run -m pytest -v .  # Run Pytest and measure test coverage
          pipenv run coverage report -m  # Generate and display coverage report
        # You can also run Pytest without coverage report using: pipenv run pytest -v .

```

This YAML file sets up a workflow named "CI Testing" that triggers on pushes to the main branch. It runs the tests using Python 3.x, installs dependencies, runs Pytest, and uploads test results.

### Step 3: Commit and Push the YAML File
Commit the fastapi-ci.yml file to your repository and push it to GitHub. The workflow will automatically be activated on pushes to the main branch.

### Step 4: Monitor CI Testing
You can monitor the progress of your CI testing workflow by visiting the "Actions" tab in your GitHub repository. There, you'll find detailed logs and information about each run.

## Conclusion

That's it! You've now set up CI testing for your FastAPI project using GitHub Actions. With CI testing in place, your code will be automatically tested every time changes are pushed to your repository, ensuring the reliability of your application.

## Further Reading

- [GitHub Actions Official Documentation](https://docs.github.com/en/actions): The official documentation is a comprehensive resource for understanding and using GitHub Actions for CI/CD.


