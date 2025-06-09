"""Workflow Configuration."""

from functools import lru_cache
from typing import Literal
from uuid import uuid4

from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

from server.clients.langfuse import trace_callback
from server.config.settings import settings


def workflow_config(user_id: str | None = None) -> dict:
    """Get the workflow configuration."""
    thread_id = str(uuid4())
    config = {
        "configurable": {
            "thread_id": thread_id,
            "user_id": user_id,
        },
        "callbacks": [trace_callback()]
    }
    return config


async def checkpointer(type: Literal["memory", "postgres"] = "memory") -> MemorySaver | AsyncPostgresSaver:
    """Get the workflow checkpointer."""
    if type == "memory":
        return MemorySaver()
    if type == "postgres":
        return await postgres_checkpointer()
    raise NotImplementedError(f"Invalid checkpointer type: {type}")

@lru_cache
async def postgres_checkpointer() -> AsyncPostgresSaver:
    """Get the postgres checkpointer."""
    saver = AsyncPostgresSaver.from_conn_string(settings().POSTGRES_CONNECTION_STRING)
    await saver.setup()
    return saver
