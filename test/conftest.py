import pytest
from starlette.testclient import TestClient

@pytest.fixture(scope="session")
def app_client() -> TestClient:
  from src.app import app
  
  with TestClient(app) as test_client:
    yield test_client
