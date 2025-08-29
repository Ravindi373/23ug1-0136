#!/usr/bin/env bash
set -euo pipefail
echo "Preparing app ..."
# Create external network & volume (idempotent)
docker network create app-net >/dev/null 2>&1 || true
docker volume create db-data >/dev/null 2>&1 || true
# Build custom images (web)
docker compose build
echo "Done."
