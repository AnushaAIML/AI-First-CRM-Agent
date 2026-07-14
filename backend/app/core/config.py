"""
Application configuration.

Loads environment variables from the .env file and exposes them
through a single settings object.
"""

from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Groq API Key
    GROQ_API_KEY: str = Field(...)

    # PostgreSQL Connection URL
    DATABASE_URL: str = Field(...)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Load settings once and reuse them throughout the app."""
    return Settings()


settings = get_settings()