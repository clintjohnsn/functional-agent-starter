"""Example Workflow."""

import logging

import ell
from langgraph.func import entrypoint, task

from server.clients.llms import llm
from server.models.states import ExampleState
from server.workflows.base import checkpointer

logger = logging.getLogger(__name__)

@entrypoint(checkpointer=checkpointer())
async def workflow(state: ExampleState) -> ExampleState:
    """Example Workflow."""
    response: str = await llm_call(state.user_msg)
    state.response = response
    return state

@task()
@ell.simple(model="gpt-4o-mini", temperature=0.7, client=llm())
def llm_call(user_msg: str) -> str:
    """You are a helpful assistant.""" # System prompt
    logger.info("Chatting to the user")
    return f"{user_msg}" # User prompt
