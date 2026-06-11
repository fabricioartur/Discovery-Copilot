"""Shared protocol for report generation clients."""

from __future__ import annotations

from typing import Protocol


class ReportGenerationClient(Protocol):
    """A client capable of turning prompts into Markdown content."""

    def generate_markdown(self, system_prompt: str, user_prompt: str) -> str:
        """Generate Markdown for one report."""
