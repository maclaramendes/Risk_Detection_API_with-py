from app.schemas import Transaction

def analyze_transaction_risk(transaction: Transaction) -> dict:
    risk_score = 0
    reasons = []

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