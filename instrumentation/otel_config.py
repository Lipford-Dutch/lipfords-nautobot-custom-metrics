"""OpenTelemetry tracing setup for tests."""
import os

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

RUN_ID = os.getenv("OTEL_TEST_RUN_ID", "local")

"""Configure tracing provider and return a tracer."""

def setup_tracing():
    resource = Resource.create({"service.name": "qa-tests", "run_id": RUN_ID})
    exporter = InMemorySpanExporter()
    provider = TracerProvider(resource=resource)
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    trace.set_tracer_provider(provider)
    return trace.get_tracer(__name__)
