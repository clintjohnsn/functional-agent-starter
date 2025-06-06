"""Example Service."""

import logging
from uuid import uuid4

from server.models.dto import ExampleRequestDTO, ExampleResponseDTO
from server.models.states import ExampleState
from server.workflows.example_workflow import workflow

logger = logging.getLogger(__name__)

class ExampleService:
    """Example Service."""

    async def chat(self, body: ExampleRequestDTO) -> ExampleResponseDTO:
        """Chat to an AI Agent."""
        state: ExampleState = ExampleState(user_msg=body.user_msg)
        thread_id: str = str(uuid4())
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }
        result: ExampleState = await workflow.ainvoke(state, config)
        return ExampleResponseDTO(response=result.response) 