"""Report generation orchestration."""

from __future__ import annotations

from pathlib import Path

from src.openai_client import DiscoveryOpenAIClient
from src.reports import REPORTS
from utils.files import ensure_directory, read_prompt, write_markdown


PROMPTS_DIR = Path("prompts")
OUTPUT_DIR = Path("output")


def generate_reports(document: str, client: DiscoveryOpenAIClient) -> list[Path]:
    """Generate all Discovery Copilot reports and return written paths."""

    ensure_directory(OUTPUT_DIR)

    system_prompt = read_prompt(PROMPTS_DIR / "system_prompt.md")
    report_template = read_prompt(PROMPTS_DIR / "report_prompt.md")

    written_files: list[Path] = []
    for report in REPORTS:
        user_prompt = report_template.format(
            title=report.title,
            instructions=report.instructions,
            document=document,
        )
        content = client.generate_markdown(system_prompt, user_prompt)
        destination = OUTPUT_DIR / report.filename
        write_markdown(destination, content)
        written_files.append(destination)

    return written_files
