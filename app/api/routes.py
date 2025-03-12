"""API routes definition."""

from typing import Dict, List

from fastapi import APIRouter, Depends, HTTPException

from app.api.models import Item, ItemCreate
from app.services.service import ItemService, get_item_service

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@router.get("/items", response_model=List[Item])
async def get_items(service: ItemService = Depends(get_item_service)) -> List[Item]:
    """Get all items."""
    return service.get_all_items()


@router.post("/items", response_model=Item, status_code=201)
async def create_item(
    item: ItemCreate, service: ItemService = Depends(get_item_service)
) -> Item:
    """Create a new item."""
    return service.create_item(item)


@router.get("/items/{item_id}", response_model=Item)
async def get_item(
    item_id: str, service: ItemService = Depends(get_item_service)
) -> Item:
    """Get item by ID."""
    item = service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
