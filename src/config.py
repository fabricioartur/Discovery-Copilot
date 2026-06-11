"""Runtime configuration helpers."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from src.exceptions import ConfigurationError

# Supported models and the trade-off rationale used when advising customers
# which model to choose for their own OpenAI deployments.
MODEL_CHOICES: dict[str, str] = {
    "gpt-5.4-mini": "Fast, cost-efficient ($0.75/$4.50 per MTok). Best default for routine discovery notes.",
    "gpt-5.4":      "High quality ($2.50/$15 per MTok). Use for complex enterprise accounts or final reports.",
    "gpt-5.5":      "Frontier model ($5/$30 per MTok). Best for strategic accounts and board-level deliverables.",
}

DEFAULT_MODEL = "gpt-5.4-mini"


REASONING_CHOICES = ("low", "medium", "high", "extra_high")


@dataclass(frozen=True)
class Settings:
    """Application settings loaded from the environment."""

    openai_api_key: str
    model: str = DEFAULT_MODEL
    reasoning_effort: str | None = None


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


def load_settings(
    model_override: str | None = None,
    reasoning_override: str | None = None,
) -> Settings:
    """Load settings from .env and the process environment.

    Args:
        model_override: When provided (e.g. from --model CLI flag), takes
            precedence over the OPENAI_MODEL environment variable.
        reasoning_override: Reasoning effort level from --reasoning CLI flag.
            One of: low, medium, high, extra_high.
    """

    _load_dotenv_if_available()
    api_key = os.getenv("OPENAI_API_KEY", "").strip()

    if not api_key:
        raise ConfigurationError(
            "OPENAI_API_KEY is missing. Create a .env file from .env.example "
            "and add your OpenAI API key."
        )

    model = (
        model_override
        or os.getenv("OPENAI_MODEL", DEFAULT_MODEL).strip()
        or DEFAULT_MODEL
    )

    if model not in MODEL_CHOICES:
        valid = ", ".join(MODEL_CHOICES)
        raise ConfigurationError(
            f"Unknown model '{model}'. Supported models: {valid}."
        )

    if reasoning_override is not None and reasoning_override not in REASONING_CHOICES:
        valid_r = ", ".join(REASONING_CHOICES)
        raise ConfigurationError(
            f"Unknown reasoning effort '{reasoning_override}'. Valid options: {valid_r}."
        )

    return Settings(openai_api_key=api_key, model=model, reasoning_effort=reasoning_override)
