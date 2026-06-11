"""OpenAI API wrapper for report generation."""

from __future__ import annotations

from src.config import Settings
from src.exceptions import ReportGenerationError


class DiscoveryOpenAIClient:
    """Small wrapper around the OpenAI Responses API."""

    def __init__(self, settings: Settings) -> None:
        try:
            from openai import OpenAI
        except ModuleNotFoundError as exc:
            raise ReportGenerationError(
                "The OpenAI package is not installed. Run: pip install -r requirements.txt"
            ) from exc

        self._client = OpenAI(api_key=settings.openai_api_key)
        self._model = settings.model

    def generate_markdown(self, system_prompt: str, user_prompt: str) -> str:
        """Generate Markdown content for one report."""

        try:
            from openai import APIConnectionError, APIStatusError, RateLimitError

            response = self._client.responses.create(
                model=self._model,
                input=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.2,
            )
        except RateLimitError as exc:
            raise ReportGenerationError(
                "OpenAI rate limit reached. Wait a moment and try again."
            ) from exc
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

        content = response.output_text.strip()
        if not content:
            raise ReportGenerationError("OpenAI returned an empty response.")

        return content
