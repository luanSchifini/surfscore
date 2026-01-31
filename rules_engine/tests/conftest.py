import pytest
from fastapi.testclient import TestClient
from rules_engine.src.main import app


@pytest.fixture(scope="module")
def client():
    """
    Fixture to create a TestClient for FastAPI app.
    """
    with TestClient(app) as test_client:
        yield test_client