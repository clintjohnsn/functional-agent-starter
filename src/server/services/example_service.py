"""Example Service."""

import logging

from server.models.dto import ExampleRequestDTO, ExampleResponseDTO
from server.models.states import ExampleState
from server.workflows.base import workflow_config
from server.workflows.example_workflow import workflow

logger = logging.getLogger(__name__)

class ExampleService:
    """Example Service."""

    async def chat(self, body: ExampleRequestDTO) -> ExampleResponseDTO:
        """Chat to an AI Agent."""
        state: ExampleState = ExampleState(user_msg=body.user_msg)
        result: ExampleState = await workflow.ainvoke(state, config=workflow_config())
        return ExampleResponseDTO(response=result.response)
