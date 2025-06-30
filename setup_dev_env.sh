#!/bin/bash
# Setup the Nautobot custom metrics development environment
# Based on docs/dev/dev_environment.md Quickstart instructions
set -e

# Ensure required tools are installed
command -v poetry >/dev/null 2>&1 || { echo >&2 "Poetry is required. Install from https://python-poetry.org/docs/#installation"; exit 1; }
command -v docker >/dev/null 2>&1 || { echo >&2 "Docker is required. Install from https://docs.docker.com/get-docker/"; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo >&2 "docker-compose is required. Install from https://github.com/docker/compose"; exit 1; }

# Install dependencies
poetry install

# Copy example credentials if missing
if [ ! -f development/creds.env ]; then
  cp development/creds.example.env development/creds.env
fi

# Build and start Nautobot
poetry run invoke build
poetry run invoke start

cat <<MSG
Environment started.
Nautobot available at http://localhost:8080
Documentation available at http://localhost:8001
Use 'poetry run invoke stop' to stop containers and 'poetry run invoke destroy' to remove them.
MSG
