"""Tests for DiscoveryOpenAIClient error handling."""

from __future__ import annotations

import sys
import types
import unittest
from unittest.mock import MagicMock, patch

from src.config import Settings
from src.exceptions import ReportGenerationError


def _make_openai_stub(side_effects: list | None = None, return_value: str | None = None):
    """Return a minimal stub of the openai module for patching."""
    stub = types.ModuleType("openai")

    class _RateLimitError(Exception):
        pass

    class _APIConnectionError(Exception):
        pass

    class _APIStatusError(Exception):
        def __init__(self, msg="", status_code=500):
            super().__init__(msg)
            self.status_code = status_code

    stub.RateLimitError = _RateLimitError
    stub.APIConnectionError = _APIConnectionError
    stub.APIStatusError = _APIStatusError

    mock_response = MagicMock()
    mock_response.output_text = return_value or "# Report\n\nContent."

    mock_create = MagicMock()
    if side_effects:
        mock_create.side_effect = side_effects
    else:
        mock_create.return_value = mock_response

    stub.OpenAI = MagicMock(
        return_value=MagicMock(responses=MagicMock(create=mock_create))
    )
    stub._mock_create = mock_create
    stub._RateLimitError = _RateLimitError
    stub._APIConnectionError = _APIConnectionError
    stub._APIStatusError = _APIStatusError
    return stub


class TestDiscoveryOpenAIClient(unittest.TestCase):

    def _settings(self, model="gpt-4o-mini") -> Settings:
        return Settings(openai_api_key="sk-test", model=model)

    def _make_client(self, stub):
        sys.modules["openai"] = stub
        from src.openai_client import DiscoveryOpenAIClient
        client = DiscoveryOpenAIClient(self._settings())
        client._client = stub.OpenAI.return_value
        return client

    def test_successful_generation(self):
        stub = _make_openai_stub(return_value="# Report\n\nContent.")
        client = self._make_client(stub)
        result = client.generate_markdown("system", "user")
        self.assertEqual(result, "# Report\n\nContent.")

    def test_empty_response_raises(self):
        stub = _make_openai_stub(return_value="   ")
        client = self._make_client(stub)
        with self.assertRaises(ReportGenerationError) as ctx:
            client.generate_markdown("system", "user")
        self.assertIn("empty", str(ctx.exception).lower())

    def test_connection_error_raises_immediately(self):
        stub = _make_openai_stub()
        stub._mock_create.side_effect = stub._APIConnectionError("timeout")
        client = self._make_client(stub)
        with self.assertRaises(ReportGenerationError) as ctx:
            client.generate_markdown("system", "user")
        self.assertIn("connect", str(ctx.exception).lower())
        self.assertEqual(stub._mock_create.call_count, 1)

    def test_api_status_error_raises(self):
        stub = _make_openai_stub()
        stub._mock_create.side_effect = stub._APIStatusError("bad request", status_code=400)
        client = self._make_client(stub)
        with self.assertRaises(ReportGenerationError) as ctx:
            client.generate_markdown("system", "user")
        self.assertIn("400", str(ctx.exception))

    @patch("time.sleep", return_value=None)
    def test_rate_limit_retries_then_raises(self, mock_sleep):
        stub = _make_openai_stub()
        stub._mock_create.side_effect = stub._RateLimitError("rate limit")
        client = self._make_client(stub)
        with self.assertRaises(ReportGenerationError) as ctx:
            client.generate_markdown("system", "user")
        self.assertIn("rate limit", str(ctx.exception).lower())
        self.assertEqual(stub._mock_create.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)

    @patch("time.sleep", return_value=None)
    def test_rate_limit_succeeds_on_retry(self, _mock_sleep):
        stub = _make_openai_stub()
        ok_response = MagicMock()
        ok_response.output_text = "# Report\n\nOK."
        stub._mock_create.side_effect = [
            stub._RateLimitError("rate limit"),
            ok_response,
        ]
        client = self._make_client(stub)
        result = client.generate_markdown("system", "user")
        self.assertEqual(result, "# Report\n\nOK.")
        self.assertEqual(stub._mock_create.call_count, 2)

    def test_unexpected_exception_raises(self):
        stub = _make_openai_stub()
        stub._mock_create.side_effect = ValueError("unexpected")
        client = self._make_client(stub)
        with self.assertRaises(ReportGenerationError) as ctx:
            client.generate_markdown("system", "user")
        self.assertIn("unexpected", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
