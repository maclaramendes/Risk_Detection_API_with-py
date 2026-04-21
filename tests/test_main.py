from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_transaction_approved():
    response = client.post("/transaction", json={
        "amount": 100,
        "country": "BR",
        "card_country": "BR",
        "hour": 14
    })

    assert response.status_code == 200
    assert response.json()["status"] == "approved"


def test_transaction_high_amount_flagged():
    response = client.post("/transaction", json={
        "amount": 1500,
        "country": "BR",
        "card_country": "BR",
        "hour": 14
    })

    assert response.status_code == 200
    assert response.json()["status"] == "flagged"

def test_transaction_country_mismatch():
    response = client.post("/transaction", json={
        "amount": 100,
        "country": "BR",
        "card_country": "US",
        "hour": 14
    })

    assert response.status_code == 200
    assert "country_mismatch" in response.json()["reasons"]

def test_transaction_odd_hour():
    response = client.post("/transaction", json={
        "amount": 100,
        "country": "BR",
        "card_country": "BR",
        "hour": 2
    })

    assert response.status_code == 200
    assert "odd_hour" in response.json()["reasons"]

