---
paths:
  - "**/*.sql"
  - "**/migrations/**"
  - "**/migration/**"
  - "**/schema.prisma"
  - "**/flyway/**"
  - "**/liquibase/**"
  - "**/seeds/**"
  - "**/seeders/**"
---
<!-- dev-suite-managed -->

# Database Agents

When working on files matching the paths above, prefer these agents:

- `@sql-expert` — SQL specialist for database design, query optimization, stored procedures, and migrations across PostgreSQL, MySQL, Oracle, and SQL Server. Executes code modifications directly unless explicitly asked for analysis only.

Use the Task tool with the corresponding subagent_type to delegate work to these specialists.
