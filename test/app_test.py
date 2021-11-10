import pytest
from starlette.testclient import TestClient

def test_hello(app_client: TestClient):
  response = app_client.get("/")
  assert response.status_code == 200

  assert response.json()["Hello"] == "World"
