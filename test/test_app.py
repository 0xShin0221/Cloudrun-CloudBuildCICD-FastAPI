from fastapi.testclient import TestClient

from app import main

client = TestClient(main.app)


def test_get_index() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_post_index() -> None:
    response = client.post("/health")
    assert response.status_code == 405
