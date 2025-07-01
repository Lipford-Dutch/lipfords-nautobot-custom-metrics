from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

import instrumentation.otel_config as otel_config
from instrumentation.otel_config import setup_tracing


def test_setup_tracing_sets_provider(monkeypatch):
    captured = {}
    monkeypatch.setattr(otel_config, "RUN_ID", "test123")
    def fake_set_provider(provider):
        captured["provider"] = provider
    monkeypatch.setattr(trace, "set_tracer_provider", fake_set_provider)
    tracer = setup_tracing()
    provider = captured["provider"]
    assert isinstance(provider, TracerProvider)
    assert provider.resource.attributes["service.name"] == "qa-tests"
    assert provider.resource.attributes["run_id"] == "test123"
    assert tracer is not None

