<!-- DEV-SUITE-CONFIG-START -->
# Dev-Suite Configuration

## Installed Agents

- `@fastapi-expert`
- `@architect`
- `@code-reviewer`
- `@python-expert`
- `@sql-expert`
- `@ux-expert`
- `@devops-expert`
- `@integration-validator-expert`
- `@open-source-expert`
- `@qa-expert`
- `@python-integration-test-expert`

## Agent Routing (Always Active)

These agents apply to every file in the project:

- Use `@architect` for: Software architect for system design across domains — not just web/enterprise. Covers low-level/systems architecture (OS & kernels, embedded/RTOS, systems networking, storage engines, distributed consensus, virtualization, hardware-aware design), AI-integrated systems (edge inference, serving topology, hybrid edge-cloud, model gateways, agentic), data-intensive platforms, and security architecture — in addition to the classic web/enterprise patterns. Analyzes requirements, proposes architectures, and evaluates trade-offs. Use for architectural decisions, system design, and technical planning in ANY domain.
- Use `@code-reviewer` for: Code review expert for quality, security, and best practices. Analyzes code for issues, suggests improvements, and ensures adherence to standards. Use for code reviews and quality checks.
- Use `@python-expert` for: Python language expert (3.10-3.14). Covers modern typing (PEP 695), async patterns, package management (uv, poetry), CLI development (Typer), and best practices. Executes code modifications directly unless explicitly asked for analysis only.
- Use `@integration-validator-expert` for: API integration validator with feedback loop orchestration. Detects frontend API calls, validates against OpenAPI specs, and coordinates fix implementation via specialized agents. Continues validation until all contracts align. Token-efficient: queries specific endpoints only.
- Use `@open-source-expert` for: Open source readiness expert for project configuration, licensing, community health, and compliance. Executes open-source setup directly unless explicitly asked for analysis only.
- Use `@qa-expert` for: Quality Assurance expert for code quality, static analysis, and best practices. Executes quality fixes directly unless explicitly asked for analysis only.

**Important**: Always delegate tasks to the most appropriate specialist agent.

## Path-Scoped Agent Rules

The following agents activate automatically when you open matching files.
Full routing details are in the rule files listed below:

- **backend**: `@fastapi-expert` — see `.claude/rules/backend.md`
- **database**: `@sql-expert` — see `.claude/rules/database.md`
- **frontend**: `@ux-expert` — see `.claude/rules/frontend.md`
- **infrastructure**: `@devops-expert` — see `.claude/rules/infrastructure.md`
- **testing**: `@python-integration-test-expert` — see `.claude/rules/testing.md`

## API Integration Validation

This project uses `integration-validator-expert` to validate API contract consistency between frontend and backend.

### How It Works
An automatic hook (`.claude/settings.json`) detects when API endpoints or frontend integrations are modified and triggers validation automatically.

### Monitored Agents
- **Backend**: `fastapi-expert`
- **Frontend**: `typescript-expert`

### What Gets Validated
- Path/method correspondence between frontend calls and OpenAPI spec
- Request/response type alignment
- Required/optional field correctness

### Trigger Conditions
The validator is triggered when:
- Backend: Controller/route/handler modifications, new REST/GraphQL endpoints, DTO changes
- Frontend: New API calls (fetch, axios, useQuery), API type modifications

The validator is NOT triggered for:
- CSS/styling changes only
- Text/label changes only
- Internal refactoring without API changes
- UI components without data fetching

## Commands

- `/init-project` - Reconfigure dev-suite
- `/uninstall-dev-suite` - Remove dev-suite
<!-- DEV-SUITE-CONFIG-END -->
