from pydantic import BaseModel
from typing import List

class Transaction(BaseModel):
    amount: float
    country: str
    card_country: str
    hour: int

class RiskResponse(BaseModel):
    status: str
    risk_score: int
    reasons: List[str]