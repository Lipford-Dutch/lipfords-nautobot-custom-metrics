# Plugin Test Suite

## Who
Network to Code QA Team

## What
Integration tests for the Nautobot plugin endpoints and API access.

## When/Where
Run during CI with Nautobot installed via `nautobot-server test tns_custom_metrics`.

## Inputs & Outputs
Uses Django database with factories (`UserFactory`, `TokenFactory`, requiring `factory-boy`). Expects HTTP 200 responses.

## Best Practices
Implemented as `unittest`/`django.test.TestCase`-derived classes executed by the Django test runner.
