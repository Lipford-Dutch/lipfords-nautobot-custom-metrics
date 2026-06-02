# Test Suite Overview

## Who
Network to Code QA Team

## What
Unit tests for helper modules including task utilities and instrumentation.

## When/Where
Executed via `pre-commit` and during CI pipelines.

## Inputs & Outputs
Key fixtures: `otel_span` from `conftest.py` and various module fixtures.
Tests expect quick execution (<1s) and return basic assertions.

## Best Practices
All tests are marked with `@pytest.mark.unit` and follow Ruff and Black linting rules. Use `pytest -q` for fast runs.
