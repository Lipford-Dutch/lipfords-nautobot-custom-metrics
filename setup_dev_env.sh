#!/bin/bash
# Setup the Nautobot custom metrics development environment.
# Aligned to Nautobot plugin development guidance and this repo's documented workflow.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

require_command() {
  local cmd="$1"
  local hint="$2"
  command -v "$cmd" >/dev/null 2>&1 || {
    echo "ERROR: Required command '$cmd' is not installed. $hint" >&2
    exit 1
  }
}

require_command poetry "Install from https://python-poetry.org/docs/#installation"
require_command docker "Install from https://docs.docker.com/get-docker/"

if command -v docker-compose >/dev/null 2>&1; then
  COMPOSE_CMD=(docker-compose)
elif docker compose version >/dev/null 2>&1; then
  COMPOSE_CMD=(docker compose)
else
  echo "ERROR: Docker Compose is required (either 'docker-compose' or 'docker compose')." >&2
  exit 1
fi

if [ ! -f "development/development.env" ]; then
  echo "ERROR: Missing required file development/development.env" >&2
  exit 1
fi

if [ ! -f "development/creds.env" ]; then
  cat > development/creds.env <<'CREDS'
# Local development-only placeholder credentials.
# Replace these values as needed for your environment.
NAUTOBOT_DB_PASSWORD=nautobot
NAUTOBOT_REDIS_PASSWORD=
NAUTOBOT_SECRET_KEY=dev-not-for-production-change-me
NAUTOBOT_NAPALM_USERNAME=
NAUTOBOT_NAPALM_PASSWORD=
CREDS
  echo "Created development/creds.env with safe local defaults."
fi

poetry install

# Validate Docker Compose configuration before building/starting.
"${COMPOSE_CMD[@]}" -f development/docker-compose.base.yml -f development/docker-compose.dev.yml config >/dev/null

poetry run invoke build
poetry run invoke start

cat <<MSG
Environment started.
Nautobot:      http://localhost:8080
Documentation: http://localhost:8001

Useful commands:
  poetry run invoke stop
  poetry run invoke destroy
  ${COMPOSE_CMD[*]} ps
MSG
