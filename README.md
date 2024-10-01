<p align="center">
  <img src="https://github.com/user-attachments/assets/d9c35359-704d-4514-87fa-d315b5577fb0" />
</p>

# Team-15-Backend
Repository for the backend of the UniTrade mobile app of Team 15.

Access to other repositories and documentation regarding the project can be found on the [central repository](https://github.com/fedemelo/Team-15-Wiki).

## Description

RESTful API to aid the UniTrade mobile application. The API is built using FastAPI, a modern Python web framework that allows to build efficient and scalable APIs.

## Installation

### Requirements

- Python 3.8 or higher
- pip (Python package manager)
- virtualenv (Python virtual environment manager)

## Local Development Setup

The project must be run using [Python 3.11.3](https://www.python.org/downloads/release/python-3113/).

1. Create a virtual environment

   ```shell
   python -m venv venv
   ```

2. Activate the virtual environment

   Unix:

   ```shell
   source venv/bin/activate
   ```

   Windows:

   ```batch
   venv\Scripts\activate.bat
   ```

3. Install dependencies

   ```shell
   pip install -r requirements.txt
   ```

4. Run the application

Run the application using the following command:
```bash
uvicorn src.main:app --reload
```

The application will be running on http://127.0.0.1:8000/.

## API Documentation

The API documentation is available at http://127.0.0.1:8000/, created automatically by Swagger UI.