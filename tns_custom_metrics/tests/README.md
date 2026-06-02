# Plugin Test Suite

## Who
Network to Code QA Team

## What
Integration tests for the Nautobot plugin endpoints and API access.

## When/Where
Run during CI with Nautobot installed. Skipped otherwise.

## Inputs & Outputs
Uses Django database with factories (`UserFactory`, `TokenFactory`). Expects HTTP 200 responses.

## Best Practices
Tagged with `@pytest.mark.integration` and executed via `TransactionTestCase`-derived classes when jobs are involved.
