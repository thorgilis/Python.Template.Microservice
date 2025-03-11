"""Service layer for business logic."""
from typing import Dict, List, Optional
from datetime import datetime

from app.api.models import Item, ItemCreate


class ItemService:
    """Service for handling item operations."""
    
    def __init__(self) -> None:
        """Initialize the service with an in-memory store."""
        self.items: Dict[str, Item] = {}
    
    def get_all_items(self) -> List[Item]:
        """Get all items."""
        return list(self.items.values())
    
    def get_item_by_id(self, item_id: str) -> Optional[Item]:
        """Get item by ID."""
        return self.items.get(item_id)
    
    def create_item(self, item_create: ItemCreate) -> Item:
        """Create a new item."""
        item = Item(**item_create.model_dump())
        self.items[item.id] = item
        return item
    
    def update_item(self, item_id: str, item_data: ItemCreate) -> Optional[Item]:
        """Update an existing item."""
        if item_id not in self.items:
            return None
        
        updated_item = self.items[item_id].copy(update={
            **item_data.model_dump(),
            "updated_at": datetime.now(datetime.timezone.utc)
        })
        
        self.items[item_id] = updated_item
        return updated_item
    
    def delete_item(self, item_id: str) -> bool:
        """Delete an item."""
        if item_id not in self.items:
            return False
        
        del self.items[item_id]
        return True
    
# Create a singleton instance
item_service = ItemService()


def get_item_service() -> ItemService:
    """Get the singleton ItemService instance."""
    return item_service