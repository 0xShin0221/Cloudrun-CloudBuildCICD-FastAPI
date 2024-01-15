from fastapi.testclient import TestClient
import pytest
from app import main as fastapi_app


@pytest.fixture
def app():
    yield fastapi_app


@pytest.fixture
def client(app):
    with TestClient(app) as client:
        yield client
