# Pull the base docker image of python with tag 3.10.12
FROM python:3.10.12

# Install Pipenv
RUN pip install pipenv

# Change the working dir inside the container - cd /app
WORKDIR /app

# Copy main.py as source cod and req.txt as dependency
COPY . ./

# Install the dependency
RUN pipenv install --system --deploy --ignore-pipfile

### Container Env same as local at this point
EXPOSE 80

CMD ["streamlit", "run", "main.py", "--server.port", "80"]