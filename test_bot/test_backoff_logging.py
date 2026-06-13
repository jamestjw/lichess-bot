"""Tests for backoff logging."""

import logging

import pytest

from lib import lichess


def test_backoff_handler_logs_call_args(caplog: pytest.LogCaptureFixture) -> None:
    """Test that the backoff handler avoids reserved LogRecord keys."""
    details = {
        "target": test_backoff_handler_logs_call_args,
        "args": ("game-id",),
        "kwargs": {"data": "move=e2e4"},
        "tries": 1,
        "elapsed": 0.0,
        "wait": 0.1,
    }

    with caplog.at_level(logging.DEBUG):
        lichess.backoff_handler(details)

    backoff_record = next(record for record in caplog.records if record.getMessage() == "backoff_retry")
    assert backoff_record.call_args == ("game-id",)
