"""Pytest configuration with OpenTelemetry spans."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

try:
    from instrumentation.otel_config import setup_tracing
except ModuleNotFoundError:  # pragma: no cover - optional dependency missing
    class _DummySpan:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    class _DummyTracer:
        def start_as_current_span(self, name):  # noqa: D401
            """Return a dummy span when OpenTelemetry isn't installed."""

            return _DummySpan()

    def setup_tracing():  # type: ignore[override]
        return _DummyTracer()


@pytest.fixture(autouse=True)
def otel_span(request):
    """Start a tracing span around each test."""
    tracer = setup_tracing()
    name = f"qa.{request.module.__name__}.{request.node.name}"
    with tracer.start_as_current_span(name):
        yield
