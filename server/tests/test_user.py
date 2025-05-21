import pytest
from fastapi.testclient import TestClient
from mahjong.app.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_create_user(client):
    response = client.post("/users/", json={"username": "testuser", "email": "testuser@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_get_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_update_user(client):
    response = client.put("/users/1", json={"username": "updateduser"})
    assert response.status_code == 200
    assert response.json()["username"] == "updateduser"

def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
