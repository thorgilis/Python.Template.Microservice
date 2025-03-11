"""Test fixtures and configuration."""
import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the application."""
    return TestClient(app)