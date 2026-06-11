"""File-system helpers."""

from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not already exist."""

    path.mkdir(parents=True, exist_ok=True)


def read_prompt(path: Path) -> str:
    """Read a prompt template from disk."""

    return path.read_text(encoding="utf-8").strip()


def write_markdown(path: Path, content: str) -> None:
    """Write Markdown content with a trailing newline."""

    path.write_text(content.strip() + "\n", encoding="utf-8")
