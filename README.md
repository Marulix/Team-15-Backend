<p align="center">
  <img src="https://github.com/user-attachments/assets/d9c35359-704d-4514-87fa-d315b5577fb0" />
</p>

# Team-15-Backend
Repository for the backend of the UniTrade mobile app of Team 15.

Access to other repositories and documentation regarding the project can be found on the [central repository](https://github.com/fedemelo/Team-15-Wiki).

## Description

RESTful API to aid the UniTrade mobile application. The API is built using FastAPI, a modern Python web framework that allows to build efficient and scalable APIs.

## Local Development Setup with Docker

### Prerequisites

- Docker installed on your local machine. You can follow the instructions [here](https://docs.docker.com/get-docker/).

### Steps

1. Build the Docker image:

   ```bash
   docker compose build --no-cache
   ```


2. Run the Docker container:

   ```bash
   docker-compose up
   ```

3. The API will be available at `http://127.0.0.1:8000`.
4. The API documentation will be available at `http://127.0.0.1:8000/docs`.
