"""LLM Client."""

from functools import lru_cache

from openai import OpenAI

from server.config.settings import settings

config = settings()

@lru_cache
def llm() -> OpenAI:
    """Get the OpenAI LLM client."""
    return OpenAI(api_key=config.OPENAI_API_KEY)

