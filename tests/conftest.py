import pytest
from fastapi.testclient import TestClient

from cisc217_week13.main import app, characters


@pytest.fixture(autouse=True)
def reset_characters():
    characters.clear()
    characters.update(
        {
            1: {"id": 1, "name": "Aria", "health": 100, "power": 85},
            2: {"id": 2, "name": "Borin", "health": 120, "power": 70},
        }
    )
    yield


@pytest.fixture
def client():
    return TestClient(app)
