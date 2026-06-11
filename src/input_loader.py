"""Input file loading and validation."""

from __future__ import annotations

from pathlib import Path

from src.exceptions import InputError


SUPPORTED_EXTENSIONS = {".txt", ".md"}


def load_input_document(file_path: str) -> str:
    """Read and validate a supported discovery input document."""

    path = Path(file_path)

    if not path.exists():
        raise InputError(f"Input file not found: {path}")

    if not path.is_file():
        raise InputError(f"Input path is not a file: {path}")

    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        supported = ", ".join(sorted(SUPPORTED_EXTENSIONS))
        raise InputError(f"Unsupported input format. Use one of: {supported}")

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise InputError("Input file must be UTF-8 encoded text.") from exc
    except OSError as exc:
        raise InputError(f"Unable to read input file: {exc}") from exc

    if not content.strip():
        raise InputError("Input document is empty.")

    return content.strip()
