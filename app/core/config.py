"""Configuration module for the application."""
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "microservice"
    DEBUG: bool = Field(default=False)
    API_PREFIX: str = "/api"
    
    # Database
    DATABASE_URL: Optional[str] = None
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": True
    }


@lru_cache
def get_settings() -> Settings:
    """Get application settings from environment."""
    return Settings()