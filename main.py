"""Discovery Copilot command-line entrypoint."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from src.config import MODEL_CHOICES, REASONING_CHOICES, DEFAULT_MODEL, load_settings
from src.exceptions import DiscoveryCopilotError
from src.generator import generate_reports
from src.input_loader import load_input_document
from src.mock_client import MockDiscoveryClient
from src.openai_client import DiscoveryOpenAIClient


def parse_args() -> argparse.Namespace:
    model_help = "  |  ".join(f"{m}: {d}" for m, d in MODEL_CHOICES.items())
    parser = argparse.ArgumentParser(
        prog="discovery-copilot",
        description=(
            "Generate structured pre-sales discovery reports from .txt or .md "
            "customer notes using the OpenAI API."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  # Demo mode — no API key required\n"
            "  python main.py examples/northstar_retail_group/discovery_notes.md --provider mock\n\n"
            "  # Standard run with default model (gpt-4o-mini)\n"
            "  python main.py input/my_notes.md\n\n"
            "  # High-quality run for a strategic account\n"
            "  python main.py input/my_notes.md --model gpt-4o\n\n"
            "  # Frontier model for strategic accounts\n"
            "  python main.py input/my_notes.md --model gpt-5.5\n"
        ),
    )
    parser.add_argument(
        "input_file",
        help="Path to a .txt or .md discovery notes file.",
    )
    parser.add_argument(
        "--provider",
        choices=("openai", "mock"),
        default="openai",
        help=(
            "Report generation provider. Use 'mock' for local demos without "
            "an OpenAI API key. (default: openai)"
        ),
    )
    parser.add_argument(
        "--model",
        choices=list(MODEL_CHOICES),
        default=None,
        metavar="MODEL",
        help=(
            f"OpenAI model to use (default: {DEFAULT_MODEL}). "
            f"Overrides OPENAI_MODEL env var.\n{model_help}"
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="DIR",
        help="Directory for generated reports. (default: ./output)",
    )
    parser.add_argument(
        "--reasoning",
        choices=list(REASONING_CHOICES),
        default=None,
        metavar="LEVEL",
        help=(
            "Reasoning effort for GPT-5 models: low | medium | high | extra_high. "
            "Higher effort produces deeper analysis at increased cost and latency. "
            "When set, temperature is disabled (reasoning models control their own sampling)."
        ),
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging for debugging API calls.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )

    output_dir = Path(args.output) if args.output else None

    try:
        document = load_input_document(args.input_file)

        if args.provider == "mock":
            client = MockDiscoveryClient()
        else:
            settings = load_settings(model_override=args.model, reasoning_override=args.reasoning)
            client = DiscoveryOpenAIClient(settings)
            reasoning_label = f"  Reasoning: {settings.reasoning_effort}" if settings.reasoning_effort else ""
            print(f"Model: {settings.model}{reasoning_label}", file=sys.stderr)

        print(f"Generating 11 reports from: {args.input_file}", file=sys.stderr)
        written_files = generate_reports(document, client, output_dir=output_dir)

    except DiscoveryCopilotError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\nCancelled.", file=sys.stderr)
        return 130

    print("\nDiscovery reports generated:")
    for path in written_files:
        print(f"  {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
