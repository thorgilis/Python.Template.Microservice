"""API data models."""

from datetime import UTC, datetime
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


def generate_id() -> str:
    """Generate a unique ID."""
    return str(uuid4())


class ItemBase(BaseModel):
    """Base item model."""

    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)


class ItemCreate(ItemBase):
    """Item creation model."""

    pass


class Item(ItemBase):
    """Item model with ID and timestamps."""

    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: Optional[datetime] = None

    class Config:
        """Pydantic config."""

        from_attributes = True
