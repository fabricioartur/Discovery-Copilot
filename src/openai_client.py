"""OpenAI API wrapper for report generation."""

from __future__ import annotations

import logging
import time

from src.config import Settings
from src.exceptions import ReportGenerationError

logger = logging.getLogger(__name__)

_MAX_RETRIES = 3
_RETRY_BASE_DELAY = 2.0  # seconds; doubles on each attempt


class DiscoveryOpenAIClient:
    """Small wrapper around the OpenAI Responses API."""

    def __init__(self, settings: Settings) -> None:
        try:
            from openai import OpenAI
        except ModuleNotFoundError as exc:
            raise ReportGenerationError(
                "The OpenAI package is not installed. Run: pip install -r requirements.txt"
            ) from exc

        self._client = OpenAI(
            api_key=settings.openai_api_key,
            timeout=60.0,
        )
        self._model = settings.model
        self._reasoning_effort = settings.reasoning_effort

    def generate_markdown(self, system_prompt: str, user_prompt: str) -> str:
        """Generate Markdown content for one report, with retry on rate limits."""

        try:
            from openai import APIConnectionError, APIStatusError, RateLimitError
        except ModuleNotFoundError as exc:
            raise ReportGenerationError(
                "The OpenAI package is not installed. Run: pip install -r requirements.txt"
            ) from exc

        extra_kwargs: dict[str, object] = {}
        if self._reasoning_effort is not None:
            extra_kwargs["reasoning"] = {"effort": self._reasoning_effort}
        else:
            extra_kwargs["temperature"] = 0.2

        last_exc: Exception | None = None
        for attempt in range(_MAX_RETRIES):
            try:
                logger.debug("Calling OpenAI API (model=%s, attempt=%d)", self._model, attempt + 1)
                response = self._client.responses.create(
                    model=self._model,
                    input=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    **extra_kwargs,
                )
                content = response.output_text.strip()
                if not content:
                    raise ReportGenerationError("OpenAI returned an empty response.")
                return content

            except RateLimitError as exc:
                last_exc = exc
                if attempt < _MAX_RETRIES - 1:
                    delay = _RETRY_BASE_DELAY * (2 ** attempt)
                    logger.warning("Rate limit hit. Retrying in %.0fs (attempt %d/%d).", delay, attempt + 1, _MAX_RETRIES)
                    time.sleep(delay)

            except APIConnectionError as exc:
                raise ReportGenerationError(
                    "Could not connect to the OpenAI API. Check your network connection."
                ) from exc

            except APIStatusError as exc:
                raise ReportGenerationError(
                    f"OpenAI API returned an error: HTTP {exc.status_code}."
                ) from exc

            except Exception as exc:
                raise ReportGenerationError(f"Unexpected API failure: {exc}") from exc

        raise ReportGenerationError(
            f"OpenAI rate limit reached after {_MAX_RETRIES} attempts. Wait a moment and try again."
        ) from last_exc
