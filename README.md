# Risk Detection API

Simple API for transaction risk analysis, built with FastAPI.

## Features

* Health check endpoint
* Transaction analysis
* Basic fraud detection rules

## Technologies

* Python
* FastAPI
* Uvicorn
* Docker

## How to run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run with Docker

### Build image

```bash
docker build -t risk-api .
```

### Run container

```bash
docker run -d -p 8000:8000 --name risk-api-container risk-api
```

### Access API

Open in your browser:

```
http://127.0.0.1:8000/docs
```
