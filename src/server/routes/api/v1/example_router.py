"""Example API endpoints."""

from fastapi import APIRouter, Depends, Request, status

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
async def chat(request: Request, body: ExampleRequestDTO, service: ExampleService = Depends(ExampleService)) -> ExampleResponseDTO:
    """Chat to an AI Agent."""
    return await service.chat(body)