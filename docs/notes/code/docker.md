## Definitions

`Image`
: An image is a blueprint or template that encompasses all the essential files, dependencies, and configurations needed to create a running instance of a container. Think of it as a static, read-only snapshot that bundles together the application's code, necessary libraries, and the runtime environment, ensuring the application runs as intended.

`Container`
: A container is an isolated, lightweight runtime instance derived from an image. Essentially, when an image is executed, it becomes a container. Containers encapsulate the application along with its dependencies, offering a consistent and reproducible setting. This means applications can run reliably across various computing contexts, be it a developer's local machine or a production server.

## Dockerfile
```docker title="Dockerfile"
# Use the official Python 3.11 image as a parent image
FROM python:3.11

# Set the working directory inside the container to `/app`
WORKDIR /app

# Copy the project's Python dependencies file to the container
COPY pyproject.toml ./

# Copy the application's source code to the container's `/app/src` directory
COPY ./src /app/src

# Install the PDM (Python Dependency Management) tool without storing cache
RUN pip install --no-cache-dir pdm

# Use PDM to install the project's Python dependencies
RUN pdm install

# Update the PATH to ensure executables inside the virtual environment are found
ENV PATH="/app/.venv/bin:$PATH"

# Copy the MkDocs configuration file to the container
COPY mkdocs.yml ./
```

### Instructions

`RUN`
: Executes commands during the image building phase. Often used to install dependencies or to build the application.

`WORKDIR`
: Designates the working directory for subsequent commands within the Dockerfile. Essentially, it's like using cd in a terminal.

`COPY`
: Transfers files or directories from the source on the host to the container's filesystem at the set destination.

`VOLUME`
: Specifies a mount point to facilitate data sharing and persistence between the host and container.

`EXPOSE`
: Indicates the network ports the container listens to, primarily for documentation purposes.

`ENV`
: Sets environment variables which can be used by processes inside the container.

`ARG`
: Declares variables that users can pass at build-time, offering more flexibility during image creation.

`ENTRYPOINT`
: Determines the default command that will be executed when the container starts.

`CMD`
: Specifies the default command for the container when it runs, which can be overridden by command-line options.
## docker-compose

```yaml title="docker-compose.yml"
# Define the Docker Compose file version
version: "3.8"
services:
  # Define the http-server service
  http-server:
    build:
      context: . # Set the build context to the current directory
      dockerfile: Dockerfile # Specify the Dockerfile to use
    ports:
      - "8080:8080" # Map port 8080 on the host to port 8080 on the container
    command: python src/leitner/server.py # Command to run when the container starts
    volumes:
      - ./docs:/app/docs # Mount the `docs` directory from the host to `/app/docs` in the container

  # Define the mkdocs-server service
  mkdocs-server:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    command: mkdocs serve -a 0.0.0.0:8000
    volumes:
      - ./docs:/app/docs
```

## Nginx
Nginx is a versatile tool, commonly used as a web server, load balancer, or reverse proxy. In a Docker environment, Nginx can be containerized and configured to direct traffic to other containers, ensuring efficient communication and load distribution.

### Dockerizing Nginx

```dockerfile title="Dockerfile.nginx"
# Use the official Nginx image as a base
FROM nginx:latest

# Copy custom configuration to Nginx
COPY nginx.conf /etc/nginx/nginx.conf
```
For the purpose of this example, let's consider a basic nginx.conf file:

```conf title="nginx.conf"
events {}

http {
    server {
        listen 80;

        location / {
            proxy_pass http://your_backend_service_address:port;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

In the configuration above, Nginx listens on port 80 and proxies incoming requests to a backend service. You'd replace your_backend_service_address:port with the address and port of your actual backend service, which could be another Docker container.

### How to integrate Nginx with another service

```yaml title="docker-compose.yml"

version: '3.8'

services:
  nginx:
    build:
      context: .
      dockerfile: Dockerfile.nginx
    ports:
      - "80:80"

  webapp:
    image: your_web_app_image
    expose:
      - "8080"
```
In this setup, the Nginx container would proxy requests to the webapp container.

Access the application through your browser or API client on port 80, and Nginx will handle the proxying to your web application.

## Flashcards
??? question "`Docker Image`? [](){.fbutton .ok}[](){.fbutton .nok}"
    A blueprint or template containing all necessary files, dependencies, and configurations to create a running instance of a container
    ##### id: 94fb81, box: 2, score: 1/1, next: 13/10/2023, last: 12/10/2023

??? question "`Docker Container` [](){.fbutton .ok}[](){.fbutton .nok}"
    A container is a running instance of an image, encapsulating the application and its dependencies
    ##### id: 6c7265, box: 3, score: 2/2, next: 21/10/2023, last: 15/10/2023

??? question "Docker: What does the RUN instruction do in a Dockerfile [](){.fbutton .ok}[](){.fbutton .nok}"
    It executes commands during the image building phase
    ##### id: 369057, box: 3, score: 2/2, next: 18/10/2023, last: 12/10/2023

??? question "Docker: What is the purpose of COPY instruction [](){.fbutton .ok}[](){.fbutton .nok}"
    It transfers files or directories from the host to the container's filesystem
    ##### id: 208389, box: 2, score: 1/2, next: 17/10/2023, last: 16/10/2023

??? question "Docker: relation between Image and Container [](){.fbutton .ok}[](){.fbutton .nok}"
    A container is a running instance of an image, encapsulating the application and its dependencies
    ##### id: 284eba, box: 2, score: 1/1, next: 17/10/2023, last: 16/10/2023

??? question "Docker: how is WORKDIR used ? [](){.fbutton .ok}[](){.fbutton .nok}"
    It sets the working directory for subsequent commands
    ##### id: 179344, box: 3, score: 2/2, next: 18/10/2023, last: 12/10/2023

??? question "Docker: why use VOLUME instruction? [](){.fbutton .ok}[](){.fbutton .nok}"
    To specify a mount point for sharing and persisting data between the host and container.
    ##### id: a3e837, box: 2, score: 1/1, next: 16/10/2023, last: 15/10/2023

??? question "Docker: what does the EXPOSE instruction indicate? [](){.fbutton .ok}[](){.fbutton .nok}"
    It documents the network ports the container listens on
    ##### id: 227aed, box: 3, score: 2/2, next: 21/10/2023, last: 15/10/2023

??? question "Docker: how does ENV instruction benefit a Docker container? [](){.fbutton .ok}[](){.fbutton .nok}"
     It sets environment variables for processes inside the container
    ##### id: 8a8839, box: 3, score: 2/2, next: 21/10/2023, last: 15/10/2023

??? question "Docker: difference between ENTRYPOINt and CMD [](){.fbutton .ok}[](){.fbutton .nok}"
    ENTRYPOINT determines the default command when the container starts, while CMD specifies the default command for the container when it runs but can be overridden
    ##### id: 21c98d, box: 2, score: 1/1, next: 11/10/2023, last: 10/10/2023

??? question "Why use nginx in a containerzied environment? [](){.fbutton .ok}[](){.fbutton .nok}"
    To direct traffic to other containers, ensuring efficient communication and load distribution
    ##### id: 40f133, box: 3, score: 2/2, next: 22/10/2023, last: 16/10/2023

??? question "Primary use case of nginx in a Docker environment [](){.fbutton .ok}[](){.fbutton .nok}"
    As a reverse proxy to direct traffic to other containers
    ##### id: ffcc4f, box: 1, score: 0/0, next: 09/10/2023, last: 09/10/2023

??? question "How to make nginx and other service communicate in a docker-compose? [](){.fbutton .ok}[](){.fbutton .nok}"
    By defining both services in the docker-compose.yml and setting up proper networking and proxy configurations in Nginx

    ```yaml title="docker-compose.yml"
    version: '3.8'
    services:
      nginx:
        build:
          context: .
          dockerfile: Dockerfile.nginx
        ports:
          - "80:80"
      webapp:
        image: your_web_app_image
        expose:
          - "8080"
    ```
    ##### id: 113f1f, box: 1, score: 0/0, next: 09/10/2023, last: 09/10/2023