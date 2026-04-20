import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_json(client):
    response = client.get("/")
    data = response.get_json()
    assert data["app"] == "cloudnative-pipeline"
    assert data["status"] == "running"


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_ready_check(client):
    response = client.get("/ready")
    assert response.status_code == 200


def test_get_items(client):
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    data = response.get_json()
    assert "items" in data
    assert data["count"] == 3


def test_get_single_item(client):
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1


def test_item_not_found(client):
    response = client.get("/api/v1/items/999")
    assert response.status_code == 404
