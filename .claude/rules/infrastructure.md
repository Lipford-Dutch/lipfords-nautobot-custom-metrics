---
paths:
  - "Dockerfile*"
  - "docker-compose*.yml"
  - "docker-compose*.yaml"
  - ".github/workflows/**"
  - ".gitlab-ci.yml"
  - "**/*.tf"
  - "**/*.tfvars"
  - "**/k8s/**"
  - "**/kubernetes/**"
  - "**/helm/**"
  - "**/charts/**"
  - "Makefile"
  - "**/*.sh"
---
<!-- dev-suite-managed -->

# Infrastructure Agents

When working on files matching the paths above, prefer these agents:

- `@devops-expert` — DevOps and infrastructure specialist. Expert in CI/CD pipelines, container orchestration, cloud infrastructure, and deployment automation. Executes code modifications directly unless explicitly asked for analysis only.

Use the Task tool with the corresponding subagent_type to delegate work to these specialists.
