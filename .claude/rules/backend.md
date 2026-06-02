---
paths:
  - "**/*.java"
  - "**/*.kt"
  - "**/*.go"
  - "**/*.py"
  - "**/*.rs"
  - "**/*.cs"
  - "src/backend/**"
  - "src/main/**"
  - "src/server/**"
  - "backend/**"
  - "server/**"
  - "api/**"
---
<!-- dev-suite-managed -->

# Backend Agents

When working on files matching the paths above, prefer these agents:

- `@fastapi-expert` — FastAPI Python framework specialist. Expert in async Python, Pydantic models, and API design. Executes code modifications directly unless explicitly asked for analysis only.

Use the Task tool with the corresponding subagent_type to delegate work to these specialists.
