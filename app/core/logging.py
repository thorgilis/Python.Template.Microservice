"""Logging configuration for the application."""
import logging
import sys
from typing import Any, Dict

from app.core.config import get_settings

settings = get_settings()


def setup_logging() -> None:
    """Set up logging configuration."""
    log_level = getattr(logging, settings.LOG_LEVEL)
    
    logging_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "default",
                "stream": sys.stdout,
            },
        },
        "loggers": {
            "app": {"handlers": ["console"], "level": log_level},
        },
    }
    
    logging.config.dictConfig(logging_config)