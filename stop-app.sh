#!/usr/bin/env bash
set -euo pipefail
echo "Stopping app ..."
docker compose stop
echo "Stopped. Data is preserved in the 'db-data' volume."
