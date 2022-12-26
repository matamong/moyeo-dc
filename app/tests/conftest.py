from os import environ
from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.main import app


environ["APP_ENV"] = "test"


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
