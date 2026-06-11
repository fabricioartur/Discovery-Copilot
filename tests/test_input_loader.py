from __future__ import annotations

from pathlib import Path
import unittest

from src.exceptions import InputError
from src.input_loader import load_input_document


class InputLoaderTests(unittest.TestCase):
    def test_load_input_document_reads_markdown(self) -> None:
        with self.subTest("markdown file"):
            from tempfile import TemporaryDirectory

            with TemporaryDirectory() as temp_dir:
                input_file = Path(temp_dir) / "notes.md"
                input_file.write_text(
                    "# Discovery Notes\n\nCustomer context",
                    encoding="utf-8",
                )

                self.assertEqual(
                    load_input_document(str(input_file)),
                    "# Discovery Notes\n\nCustomer context",
                )

    def test_load_input_document_rejects_missing_file(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp_dir:
            with self.assertRaisesRegex(InputError, "Input file not found"):
                load_input_document(str(Path(temp_dir) / "missing.md"))

    def test_load_input_document_rejects_unsupported_extension(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "notes.pdf"
            input_file.write_text("not a real pdf", encoding="utf-8")

            with self.assertRaisesRegex(InputError, "Unsupported input format"):
                load_input_document(str(input_file))

    def test_load_input_document_rejects_empty_file(self) -> None:
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temp_dir:
            input_file = Path(temp_dir) / "empty.txt"
            input_file.write_text("   \n", encoding="utf-8")

            with self.assertRaisesRegex(InputError, "Input document is empty"):
                load_input_document(str(input_file))


if __name__ == "__main__":
    unittest.main()
