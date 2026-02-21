#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "[post-create] Starte automatische Codespace-Einrichtung"

python3 -m pip install --upgrade pip
python3 -m pip install -r "$ROOT_DIR/apps/api/requirements.txt"
python3 -m pip install pip-audit

npm install -g live-server

if [ -f "$ROOT_DIR/apps/web/package-lock.json" ]; then
  npm --prefix "$ROOT_DIR/apps/web" ci
else
  npm --prefix "$ROOT_DIR/apps/web" install
fi

if [ -f "$ROOT_DIR/apps/drawio-extension/package-lock.json" ]; then
  npm --prefix "$ROOT_DIR/apps/drawio-extension" ci
else
  npm --prefix "$ROOT_DIR/apps/drawio-extension" install
fi

echo "[post-create] Einrichtung abgeschlossen"
