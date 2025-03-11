"""Main application entry point."""
from fastapi import FastAPI
import logging

from app.api.routes import router as api_router
from app.core.config import get_settings
from app.core.logging import setup_logging

# Set up logging
setup_logging()
logger = logging.getLogger(__name__)

# Get application settings
settings = get_settings()

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

# Add API routes
app.include_router(api_router, prefix=settings.API_PREFIX)


@app.on_event("startup")
async def startup_event() -> None:
    """Run startup logic."""
    logger.info("Starting up %s", settings.APP_NAME)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    """Run shutdown logic."""
    logger.info("Shutting down %s", settings.APP_NAME)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )