"""Example API endpoints."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request, status

from server.middleware.limiter import limiter
from server.models.dto import ExampleRequestDTO, ExampleResponseDTO
from server.services.example_service import ExampleService

router = APIRouter()


@router.post(
    "/chat",
    response_model=ExampleResponseDTO,
    summary="Chat to an AI Agent",
    description="Chat to an AI Agent.",
    response_description="The response from the AI Agent",
    status_code=status.HTTP_200_OK,
)
@limiter.limit(["100 per day"])  # optional rate limit
async def chat(
    request: Request, body: ExampleRequestDTO, service: Annotated[ExampleService, Depends(ExampleService)]
) -> ExampleResponseDTO:
    """Chat to an AI Agent."""
    return await service.chat(body)
