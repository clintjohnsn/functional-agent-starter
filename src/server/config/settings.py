"""Server settings."""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Server settings."""

    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "<PROJECT NAME> APIs"
    PROJECT_DESCRIPTION: str = "<PROJECT DESCRIPTION> APIs"
    VERSION: str = "0.1.0"

    # Environment
    ENV: str = "dev"
    # Logging
    LOG_LEVEL: str = "INFO"

    # API Keys
    OPENAI_API_KEY: str

    # CORS Configuration
    BACKEND_CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173"

    @property
    def cors_origins(self) -> list[str]:
        """Return CORS origins as a list."""
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",") if origin.strip()]

    @property
    def cors_config(self) -> dict:
        """Return CORS configuration dictionary."""
        return {
            "allow_origins": self.cors_origins,
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def settings() -> Settings:
    """Get the Server settings."""
    return Settings()
