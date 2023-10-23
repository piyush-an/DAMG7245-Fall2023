# Pull the base docker image of python with tag 3.10.12
FROM python:3.12

# Install Pipenv
RUN pip install pipenv

# Change the working dir inside the container - cd /app
WORKDIR /app

# Copy main.py as source cod and req.txt as dependency
COPY main.py ./

COPY Pipfile Pipfile.lock ./
# Install the dependency
RUN pipenv install --system --deploy --ignore-pipfile

### Container Env same as local at this point
EXPOSE 8000

CMD ["gunicorn" ,"-w", "4", "-k", "uvicorn.workers.UvicornWorker" , "--bind", "0.0.0.0:8000", "main:app"]
# gunicorn command to run the service with 4 worker nodes binding localhost/0.0.0.0 on port 8000 refering app inside the main.py