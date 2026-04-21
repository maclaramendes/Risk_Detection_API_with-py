# Risk Detection API

Simple API for transaction risk analysis, built with FastAPI.

## Features
- Health check endpoint
- Transaction analysis
- Basic fraud detection rules

## Technologies
- Python
- FastAPI
- Uvicorn

## How to run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
