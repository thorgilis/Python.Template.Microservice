"""Main application entry point."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import router as api_router
from app.core.config import get_settings
from app.core.log_config import setup_logging

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)

# Get application settings
settings = get_settings()


# Define lifespan middleware
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan Handler."""
    # Startup logic
    logger.info("Starting up %s", settings.APP_NAME)
    yield
    # Shutdown logic
    logger.info("Shutting down %s", settings.APP_NAME)


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# Add API routes
app.include_router(api_router, prefix=settings.API_PREFIX)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",  # nosec B104 # Required for container deployment
        port=8000,
        reload=settings.DEBUG,
    )
