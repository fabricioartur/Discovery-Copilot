from __future__ import annotations

import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from src.generator import generate_reports
from src.mock_client import MockDiscoveryClient


class MockGenerationTests(unittest.TestCase):
    def test_generate_reports_with_mock_client(self) -> None:
        original_cwd = Path.cwd()

        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            os.chdir(tmp_path)
            try:
                prompts = tmp_path / "prompts"
                prompts.mkdir()
                (prompts / "system_prompt.md").write_text(
                    "System prompt",
                    encoding="utf-8",
                )
                (prompts / "report_prompt.md").write_text(
                    "Create the report named: {title}\n\n{instructions}\n\n{document}",
                    encoding="utf-8",
                )

                written_files = generate_reports(
                    "Northstar Retail Group discovery notes",
                    MockDiscoveryClient(),
                )
            finally:
                os.chdir(original_cwd)

            self.assertEqual(len(written_files), 11)
            self.assertTrue((tmp_path / "output" / "Executive Summary.md").exists())
            self.assertTrue(
                (tmp_path / "output" / "Discovery Quality Score.md").exists()
            )
            self.assertIn(
                "Northstar Retail Group",
                (tmp_path / "output" / "Executive Summary.md").read_text(
                    encoding="utf-8",
                ),
            )


if __name__ == "__main__":
    unittest.main()
