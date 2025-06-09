"""Langfuse Client."""

from functools import lru_cache

from langfuse.langchain import CallbackHandler

from server.config.settings import settings


@lru_cache
def trace_callback(user_id: str | None = None) -> CallbackHandler:
    """Get the Langfuse callback handler."""
    if user_id is None:
        return CallbackHandler(environment=settings().ENV)
    return CallbackHandler(user_id=user_id, environment=settings().ENV)
