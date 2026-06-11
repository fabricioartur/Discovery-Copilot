"""Runtime configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from src.exceptions import ConfigurationError


@dataclass(frozen=True)
class Settings:
    """Application settings loaded from the environment."""

    openai_api_key: str
    model: str = "gpt-4o-mini"


def _load_dotenv_if_available() -> None:
    """Load .env values without making python-dotenv mandatory at import time."""

    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        env_path = Path(".env")
        if not env_path.exists():
            return

        for line in env_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue

            key, value = stripped.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("'\""))
    else:
        load_dotenv()


def load_settings() -> Settings:
    """Load settings from .env and the process environment."""

    _load_dotenv_if_available()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

    if not api_key:
        raise ConfigurationError(
            "OPENAI_API_KEY is missing. Create a .env file from .env.example "
            "and add your OpenAI API key."
        )

    return Settings(openai_api_key=api_key, model=model)
