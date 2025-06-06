"""Test REST API."""

import httpx
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)

# def test_read_root() -> None:
#     """Test that reading the root is successful."""
#     response = client.get("")
#     assert httpx.codes.is_success(response.status_code)

def test_health_check() -> None:
    """Test that the health check endpoint is successful."""
    response = client.get("/api/v1/health")
    assert httpx.codes.is_success(response.status_code)
