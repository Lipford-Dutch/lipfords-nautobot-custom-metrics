"""Tests for the OpenTelemetry instrumentation helpers."""

import pytest

pytestmark = pytest.mark.unit

try:  # pragma: no cover - optional dependency
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
except ModuleNotFoundError:  # pragma: no cover - skip if missing
    pytest.skip("opentelemetry not installed", allow_module_level=True)

import instrumentation.otel_config as otel_config  # noqa: E402
from instrumentation.otel_config import setup_tracing  # noqa: E402


def test_setup_tracing_sets_provider(monkeypatch):
    """Verify that a tracer provider is configured and returned."""
    captured = {}

    monkeypatch.setattr(otel_config, "RUN_ID", "test123")

    def fake_set_provider(provider):
        captured["provider"] = provider

    monkeypatch.setattr(trace, "set_tracer_provider", fake_set_provider)
    tracer = setup_tracing()
    provider = captured["provider"]
    assert isinstance(provider, TracerProvider)  # noqa: S101
    assert provider.resource.attributes["service.name"] == "qa-tests"  # noqa: S101
    assert provider.resource.attributes["run_id"] == "test123"  # noqa: S101
    assert tracer is not None  # noqa: S101
