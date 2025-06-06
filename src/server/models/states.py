"""LangGraph State Models."""

from pydantic import BaseModel, Field


class BaseState(BaseModel):
    """Base workflow state."""

class ExampleState(BaseState):
    """Example workflow state."""

    user_msg: str = Field(..., max_length=10000, description="The user's message.")
    response: str | None = Field(None, description="Agent response.")