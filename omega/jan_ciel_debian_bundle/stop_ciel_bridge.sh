#!/usr/bin/env bash
set -euo pipefail
BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_FILE="$BUNDLE_DIR/ciel_bridge.pid"
if [[ -f "$PID_FILE" ]]; then
  PID="$(cat "$PID_FILE")"
  if kill -0 "$PID" 2>/dev/null; then
    kill "$PID"
    echo "[OK] Stopped bridge PID $PID"
  else
    echo "[INFO] Bridge PID file existed, but process is not running."
  fi
  rm -f "$PID_FILE"
else
  echo "[INFO] No PID file found."
fi
