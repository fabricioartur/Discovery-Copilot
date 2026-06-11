"""Application-specific exceptions."""


class DiscoveryCopilotError(Exception):
    """Base exception for expected application failures."""


class InputError(DiscoveryCopilotError):
    """Raised when an input file cannot be processed."""


class ConfigurationError(DiscoveryCopilotError):
    """Raised when required runtime configuration is missing."""


class ReportGenerationError(DiscoveryCopilotError):
    """Raised when report generation fails."""
