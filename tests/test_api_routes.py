from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_translation():
    response = client.post("/translate", json={"text": "Hello world!", "model_name": "model_1"})
    assert response.status_code == 200
    assert "translated_text" in response.json()
