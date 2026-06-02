"""OpenTelemetry tracing setup for tests."""
import os
from typing import Literal

try:
    from opentelemetry import trace  # type: ignore
    from opentelemetry.sdk.resources import Resource  # type: ignore
    from opentelemetry.sdk.trace import TracerProvider  # type: ignore
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor  # type: ignore
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fallback for test env without deps
    import contextlib

    class _DummySpan(contextlib.AbstractContextManager):
        """Minimal span context manager used when OpenTelemetry is absent."""

        def __enter__(self) -> "_DummySpan":
            return self

        def __exit__(self, exc_type, exc, tb) -> Literal[False]:  # noqa: ANN001
            return False

    class _DummyTracer:
        """Simplified tracer that yields ``_DummySpan`` instances."""

        def start_as_current_span(self, name: str) -> _DummySpan:
            return _DummySpan()

    class Resource:  # type: ignore[no-redef]
        """Container for resource attributes."""
        def __init__(self, attributes: dict):
            """Store ``attributes`` for later retrieval."""
            self.attributes = attributes

        @classmethod
        def create(cls, attrs: dict) -> "Resource":
            """Return a new :class:`Resource` from ``attrs``."""
            return cls(attrs)

    class TracerProvider:  # type: ignore[no-redef]
        """Provider that stores the attached :class:`Resource`."""
        def __init__(self, resource: Resource):
            """Create a provider for ``resource``."""
            self.resource = resource

        def add_span_processor(self, processor: object) -> None:
            """Accept a ``processor`` for API parity."""
            pass

    class SimpleSpanProcessor:  # type: ignore[no-redef]
        """No-op span processor for the dummy exporter."""
        def __init__(self, exporter: object):
            """Store ``exporter`` for API parity."""
            self.exporter = exporter

    class InMemorySpanExporter:  # type: ignore[no-redef]
        """Exporter that stores spans in memory."""
        def get_finished_spans(self) -> list:
            """Return collected spans (none for dummy)."""
            return []

    class _TraceModule:
        """Subset of the ``opentelemetry.trace`` API used in tests."""

        def __init__(self) -> None:
            self._tracer = _DummyTracer()

        def set_tracer_provider(self, provider: TracerProvider) -> None:
            self.provider = provider

        def get_tracer(self, _: str) -> _DummyTracer:
            return self._tracer

    trace = _TraceModule()

RUN_ID = os.getenv("OTEL_TEST_RUN_ID", "local")


def setup_tracing():
    """Configure a tracing provider and return a tracer."""
    resource = Resource.create({"service.name": "qa-tests", "run_id": RUN_ID})
    exporter = InMemorySpanExporter()
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(__name__)
