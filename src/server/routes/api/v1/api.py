"""REST API endpoints."""

import logging

from fastapi import APIRouter, Depends, HTTPException, status

from server.routes.api.v1.example_router import router as example_router

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1")

# Include routers
router.include_router(example_router, prefix="/example", tags=["example"])
# Other routers...


@router.get(
    "/health",
    summary="Check the health of the API",
    response_description="The health of the API",
    status_code=status.HTTP_200_OK,
)
async def health_check():
    """Check the health of the API."""
    logger.info("Health check endpoint called")
    return {"status": "up"}
