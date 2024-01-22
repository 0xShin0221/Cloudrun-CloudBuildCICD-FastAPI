from typing import Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from app import main as fastapi_app


@pytest.fixture
def app() -> Generator[FastAPI, None, None]:
    yield fastapi_app.app


@pytest.fixture
def client(app: FastAPI) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
