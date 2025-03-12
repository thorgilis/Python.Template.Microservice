"""Test fixtures and configuration."""

import os
import sys

import pytest
from fastapi.testclient import TestClient

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


@pytest.fixture
def client():
    """Create a test client for the application."""
    return TestClient(app)
