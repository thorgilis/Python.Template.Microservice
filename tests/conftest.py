"""Test fixtures and configuration."""
import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app  # Now Python should find 'app'


@pytest.fixture
def client():
    """Create a test client for the application."""
    return TestClient(app)