#!/usr/bin/env bash
set -euo pipefail
echo "Removing app ..."
# Bring down stack and remove images (not volumes, because they're external)
docker compose down --rmi all --remove-orphans
# Explicitly remove external resources created by prepare-app.sh
docker volume rm db-data >/dev/null 2>&1 || true
docker network rm app-net >/dev/null 2>&1 || true
echo "Removed app."
