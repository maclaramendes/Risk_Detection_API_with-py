# Risk Detection API

Simple API for transaction risk analysis, built with FastAPI.

## Features

* Health check endpoint
* Transaction analysis
* Basic fraud detection rules
* TDD (Test-Driven Development) applied

## Technologies

* Python
* FastAPI
* Uvicorn
* Docker
* Pytest

## How to run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run tests (TDD)

```bash
pytest -v
```

### Covered test cases

* `/health` endpoint returns 200
* Transaction approved for low risk
* High amount transactions are flagged
* Country mismatch adds risk reason
* Odd hour adds risk reason
* Invalid hour returns `422`

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
