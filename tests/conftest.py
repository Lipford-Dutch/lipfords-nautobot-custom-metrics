"""Pytest configuration with OpenTelemetry spans."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from instrumentation.otel_config import setup_tracing


@pytest.fixture(autouse=True)
def otel_span(request):
    """Start a tracing span around each test."""
    tracer = setup_tracing()
    name = f"qa.{request.module.__name__}.{request.node.name}"
    with tracer.start_as_current_span(name):
        yield
