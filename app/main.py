from fastapi import FastAPI
from app.schemas import Transaction, RiskResponse
from app.services.risk_engine import analyze_transaction_risk

app = FastAPI(title="Risk Detection API")

@app.get("/")
def read_root():
    return {"message": "Risk API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/transaction", response_model=RiskResponse)
def analyze_transaction(transaction: Transaction):
    return analyze_transaction_risk(transaction)