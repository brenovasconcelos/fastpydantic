from readline import append_history_file
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200

def test_get_all_items():
    response = client.get("/fetch-all/")

    assert response.status_code == 200

def test_get_single_item():
    response = client.get("/fetch-item/?id=5")

    assert response.status_code == 200