"""Discovery Copilot command-line entrypoint."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.config import load_settings
from src.exceptions import DiscoveryCopilotError
from src.generator import generate_reports
from src.input_loader import load_input_document
from src.openai_client import DiscoveryOpenAIClient


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        prog="Discovery Copilot",
        description=(
            "Generate structured pre-sales discovery reports from .txt or .md "
            "customer notes."
        ),
    )
    parser.add_argument(
        "input_file",
        help="Path to a .txt or .md discovery notes file.",
    )
    return parser.parse_args()


def main() -> int:
    """Run the Discovery Copilot CLI."""

    args = parse_args()

    try:
        document = load_input_document(args.input_file)
        settings = load_settings()
        client = DiscoveryOpenAIClient(settings)
        written_files = generate_reports(document, client)
    except DiscoveryCopilotError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Error: Operation cancelled by user.", file=sys.stderr)
        return 130

    print("Discovery reports generated successfully:")
    for path in written_files:
        print(f"- {Path(path)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
