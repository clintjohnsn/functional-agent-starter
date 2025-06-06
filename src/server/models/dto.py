"""Data Transfer Objects."""

from pydantic import BaseModel, Field


class ExampleRequestDTO(BaseModel):
    """Example request data transfer object."""

    user_msg: str = Field(..., max_length=10000, description="The user's message.")

class ExampleResponseDTO(BaseModel):
    """Example response data transfer object."""

    response: str = Field(..., description="AI Agent response.")
