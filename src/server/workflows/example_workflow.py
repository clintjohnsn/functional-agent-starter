"""Example Workflow."""

import logging

import ell
from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint, task

from server.clients.llms import llm
from server.models.states import ExampleState

logger = logging.getLogger(__name__)


@entrypoint(checkpointer=MemorySaver())
async def workflow(state: ExampleState) -> ExampleState:
    """Example workflow to chat to an AI Agent."""
    response: str = await hello(state.user_msg)
    state.response = response
    return state

@task()
def hello(user_msg: str) -> str:
    """You are a helpful assistant.""" # System prompt
    logger.info("Chatting to the user")
    return f"{user_msg}" # User prompt 


@task()
@ell.simple(model="gpt-4o-mini", client=llm(), temperature=0.7)
def hello_llm(user_msg: str) -> str:
    """You are a helpful assistant.""" # System prompt
    logger.info("Chatting to the user")
    return f"{user_msg}" # User prompt 