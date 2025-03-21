"""Configuration module for the application."""

import os
from functools import lru_cache
from typing import Literal

from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"  # Ignore extra env vars
    )

    APP_NAME: str = "microservice"
    DEBUG: bool = Field(default=False)
    API_PREFIX: str = "/api"

    # Required field with no default
    DATABASE_URL: str = Field(
        ..., description="Database connection string"  # ... means required (no default)
    )

    # Logging
    LOG_LEVEL: str = "INFO"

    # Environment type
    ENVIRONMENT: Literal["dev", "test", "prod"] = "dev"


class TestSettings(Settings):
    """Test settings with test-specific overrides."""

    model_config = SettingsConfigDict(
        env_file=".env.test",  # Load from test-specific file
        case_sensitive=True,
        extra="ignore",
    )

    DATABASE_URL: str = "sqlite:///./test.db"
    DEBUG: bool = True
    ENVIRONMENT: Literal["dev", "test", "prod"] = "test"


@lru_cache
def get_settings():
    """Get application settings based on environment."""
    env = os.getenv("ENVIRONMENT", "dev")

    try:
        if env.lower() == "test":
            return TestSettings()
        return Settings()
    except ValidationError as e:
        # Format and raise a more user-friendly error
        missing_fields = [
            err["loc"][0] for err in e.errors() if err["type"] == "missing"
        ]
        if missing_fields:
            error_msg = (
                f"Missing required environment variables: {', '.join(missing_fields)}"
            )
            raise ValueError(error_msg) from e
        raise
