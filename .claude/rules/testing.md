---
paths:
  - "**/*.test.*"
  - "**/*.spec.*"
  - "**/__tests__/**"
  - "**/test/**"
  - "**/tests/**"
  - "**/e2e/**"
  - "**/cypress/**"
  - "**/playwright/**"
---
<!-- dev-suite-managed -->

# Testing Agents

When working on files matching the paths above, prefer these agents:

- `@python-integration-test-expert` — Python integration testing specialist. Expert in pytest, testcontainers-python, pytest-django, FastAPI TestClient, factory_boy, Celery testing, SQLAlchemy fixtures, Alembic migration testing, HTTP mocking (respx, responses, pytest-httpserver), and contract testing with Pact. Executes test modifications directly unless explicitly asked for analysis only.

Use the Task tool with the corresponding subagent_type to delegate work to these specialists.
