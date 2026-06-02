# Skills (lazy mode)

This project uses dev-suite **tiered skill loading** to keep Claude
Code's skill description budget (`skillListingBudgetFraction`,
~1% of context) under control even with many agents installed.

- **Core skills** — declared as `core_skills:` in each agent's
  frontmatter (or `skills:` for unmigrated agents). Installed as
  native Claude Code skills under `.claude/skills/<name>/SKILL.md`.
  Claude Code auto-discovers them at boot: only the YAML description
  is loaded; the body is fetched on demand when the skill is invoked.
- **Extended skills** — declared as `extended_skills:` in each
  agent's frontmatter, plus the rest of the dev-suite catalog. NOT
  preloaded. Reachable on demand via the `skill-loader` MCP server:
  - `mcp__skill-loader__list_skills` to discover available skills
    (pass `groupByCategory: true` for a compact summary)
  - `mcp__skill-loader__load_skill({ skill_path: "<path>" })` to
    fetch a full SKILL.md body when needed

## Natively preloaded core skills (23)

- `backend-frameworks/fastapi`
- `best-practices/clean-code`
- `best-practices/git-workflow`
- `best-practices/open-source`
- `best-practices/solid-principles`
- `best-practices/token-optimization`
- `databases/sql-advanced`
- `databases/sql-fundamentals`
- `infrastructure/docker`
- `infrastructure/docker-compose`
- `infrastructure/python-packaging`
- `integration-validation/auth-flow-validation`
- `integration-validation/openapi-contract`
- `integration-validation/type-generation`
- `languages/python`
- `quality/common`
- `quality/sonarqube`
- `testing/pytest-django`
- `testing/python-integration`
- `testing/testcontainers-python`
- `ux/design-systems`
- `ux/interaction-design`
- `ux/visual-hierarchy`

> **Runtime requirement**: the `skill-loader` MCP server reads
> `DEV_SUITE_ROOT` (set to `C:\Users\wlipford\AppData\Local\Programs\@dev-suitedashboard\resources\dev-suite` in `.mcp.json`) to
> resolve non-preloaded skill bodies on demand.
