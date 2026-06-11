"""Report generation orchestration."""

from __future__ import annotations

import logging
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from src.client_protocol import ReportGenerationClient
from src.reports import REPORTS, ReportDefinition
from utils.files import ensure_directory, read_prompt, write_markdown

logger = logging.getLogger(__name__)

# Resolve paths relative to this file so the project works regardless of CWD.
_SRC_DIR = Path(__file__).parent
_PROJECT_ROOT = _SRC_DIR.parent
PROMPTS_DIR = _PROJECT_ROOT / "prompts"


def generate_reports(
    document: str,
    client: ReportGenerationClient,
    output_dir: Path | None = None,
    max_workers: int = 4,
) -> list[Path]:
    """Generate all Discovery Copilot reports and return written paths.

    Reports are generated in parallel (default: 4 threads) to reduce wall-clock
    time from ~60 s to ~15 s on a typical OpenAI API connection.
    """

    resolved_output = output_dir or (Path.cwd() / "output")
    ensure_directory(resolved_output)

    system_prompt = read_prompt(PROMPTS_DIR / "system_prompt.md")
    report_template = read_prompt(PROMPTS_DIR / "report_prompt.md")

    def _generate_one(report: ReportDefinition) -> Path:
        user_prompt = report_template.format(
            title=report.title,
            instructions=report.instructions,
            document=document,
        )
        logger.debug("Generating: %s", report.title)
        content = client.generate_markdown(system_prompt, user_prompt)
        destination = resolved_output / report.filename
        write_markdown(destination, content)
        return destination

    total = len(REPORTS)
    written_files: list[Path] = [Path()] * total
    completed = 0

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_index = {
            executor.submit(_generate_one, report): i
            for i, report in enumerate(REPORTS)
        }
        for future in as_completed(future_to_index):
            idx = future_to_index[future]
            written_files[idx] = future.result()  # propagates exceptions
            completed += 1
            print(
                f"  [{completed}/{total}] {REPORTS[idx].title}",
                flush=True,
                file=sys.stderr,
            )

    return written_files
