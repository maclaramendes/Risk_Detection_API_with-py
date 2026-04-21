from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Transaction(BaseModel):
    amount: float
    country: str
    card_country: str
    hour: int

@app.get("/")
def read_root():
    return {"message": "Risk API is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/transaction")
def analyze_transaction(transaction: Transaction):
    risk_score = 0
    reasons: List[str] = []

    if transaction.amount > 1000:
        risk_score += 50
        reasons.append("high_amount")

    if transaction.country != transaction.card_country:
        risk_score += 20
        reasons.append("country_mismatch")

    if transaction.hour < 6 or transaction.hour > 22:
        risk_score += 10
        reasons.append("odd_hour")

    status = "approved"
    if risk_score >= 50:
        status = "flagged"

    return {
        "status": status,
        "risk_score": risk_score,
        "reasons": reasons
    }