"""API tests."""
from fastapi.testclient import TestClient


def test_health_check(client: TestClient) -> None:
    """Test the health check endpoint."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item(client: TestClient) -> None:
    """Test creating an item."""
    item_data = {
        "name": "Test Item",
        "description": "This is a test item",
    }
    
    response = client.post("/api/items", json=item_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["description"] == item_data["description"]
    assert "id" in data
    assert "created_at" in data


def test_get_items(client: TestClient) -> None:
    """Test getting all items."""
    # Create an item first
    item_data = {"name": "Test Item"}
    client.post("/api/items", json=item_data)
    
    # Get all items
    response = client.get("/api/items")
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1