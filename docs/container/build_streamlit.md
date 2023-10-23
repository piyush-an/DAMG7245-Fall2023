---
tags:
  - Streamlit
  - Docker
# icon: simple/docker
---
# Dockerize Streamlit Application

## Introduction
This documentation provides a step-by-step guide on how to Dockerize a Streamlit application. Docker is a powerful tool that allows you to package your application and its dependencies into a container, ensuring consistent and reproducible deployments across different environments. By following this guide, you'll be able to containerize your Streamlit application, making it more portable and easier to manage.

## Tutorial

### Step 1: Exisitng code

Begin by moving to project directory for your Streamlit application. Ensure that your Streamlit application is working correctly in this directory before proceeding.

```bash
.
├── Pipfile
├── Pipfile.lock
└── main.py
```

### Step 2: Create Dockerfile

A Dockerfile is used to define the configuration for building a Docker image. Create a file named `Dockerfile` (with no file extension) in your project directory. Here is a sample Dockerfile for a Streamlit application:


```Dockerfile title="Dockerfile"
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
EXPOSE 8090

CMD ["streamlit", "run", "main.py", "--server.port", "8090"]
```

### Step 3: Building the Docker Image

To create a Docker image for your Streamlit application, use the docker build command. Navigate to your project directory and run the following command:

```bash
docker build -t streamlit_demo:v1 .
```

Here's a breakdown of the command:

- **`docker build`**: This command is used to build a Docker image.

- **`-t streamlit_demo:v1`**: The `-t` flag allows you to specify a name and optionally a tag for your image. In this example, we're naming the image `streamlit_demo` and giving it the tag `v1`. You can choose your own image name and tag.

- **``.`**: The dot (`.`) at the end of the command specifies the build context, which is the current directory. This tells Docker to look for the `Dockerfile` in the current directory and use it to build the image.

The Docker image will be built using the instructions in your Dockerfile. You'll see output in the terminal as each step is executed. If there are any errors during the build process, Docker will report them, and you can address them accordingly



### Step 4: Verify the Built Image

Once the build process is complete, you can verify that the image was created successfully by running:

```bash
docker images
```

You should see your newly created image listed with the name and tag you specified (streamlit_demo:v1 in this example).

```plaintext title="stdout"
REPOSITORY                     TAG       IMAGE ID       CREATED        SIZE
streamlit_demo                   v1        9e56e49d32e5   19 hours ago   1.5GB
```

### Step 5: Running the Docker Image

Now that you have built your Docker image, you can run it as a container. To do this, use the docker run command. In your terminal, navigate to the project directory, and execute the following command:

```bash
docker run -p 8090:8090 streamlit_demo:v1
```

Here's what each part of the command does:

- `**docker run**`: This command starts a Docker container based on a Docker image.
- `**-p 8090:8090**`: The `-p` flag is used to map ports between the host machine and the container. In this example, it maps port `8090` on your host to port `8090` in the container. You can adjust the host port (left side) as needed.
- `**streamlit_demo:v1**`: This specifies the Docker image you want to run. Replace streamlit_demo:v1 with the name and tag of your Docker image.


### Step 6: Access Your Streamlit Application

After running the command, your Streamlit application should be up and running inside a Docker container. You can access it by opening a web browser and navigating to: `http://localhost:8090`

<!-- ![UI](./Streamlit_ui.png) -->

### Step 7: Stopping the Container

To stop the Docker container, you can press Ctrl+C in the terminal where it is running, or you can open a new terminal window and run the following command:
```bash
docker stop <container_id_or_name>
```

Replace `container_id_or_name` with the actual container ID or name, which you can find using the docker ps command.

```bash
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS                 PORTS                                              NAMES
6f641cdaaf76   streamlit_demo:v1                "streamlit run main.…"   6 minutes ago   Up 6 minutes           0.0.0.0:8090->8090/tcp                             stoic_dijkstra
```

```bash
docker stop 6f641cdaaf76
```

## Conclusion
In this guide, you've learned how to Dockerize your Streamlit application, creating a Docker image and running it as a container. Dockerization simplifies deployment, enhances scalability, and streamlines the development process by encapsulating your application and its environment. With your Streamlit application now containerized, you have the flexibility to deploy it in various environments with confidence. This marks the beginning of a more efficient and maintainable development and deployment workflow for your Streamlit projects. Feel free to explore further Docker features and optimizations to suit your specific application needs.