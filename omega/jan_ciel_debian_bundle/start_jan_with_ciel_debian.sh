#!/usr/bin/env bash
set -euo pipefail

BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$BUNDLE_DIR/ciel_bridge.log"
PID_FILE="$BUNDLE_DIR/ciel_bridge.pid"

export CIEL_ROOT="${CIEL_ROOT:-$BUNDLE_DIR/ciel_omega}"
export CIEL_JAN_HOST="${CIEL_JAN_HOST:-127.0.0.1}"
export CIEL_JAN_PORT="${CIEL_JAN_PORT:-8080}"
export PYTHONUNBUFFERED=1

if [[ ! -d "$CIEL_ROOT" ]]; then
  echo "[ERROR] CIEL_ROOT not found: $CIEL_ROOT"
  exit 1
fi

choose_port() {
  python3 - <<'PY'
import os, socket
host = os.environ.get('CIEL_JAN_HOST', '127.0.0.1')
start = int(os.environ.get('CIEL_JAN_PORT', '8080'))
for port in range(start, start + 20):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((host, port))
        except OSError:
            continue
        print(port)
        raise SystemExit(0)
print(start)
PY
}

if [[ -f "$PID_FILE" ]] && kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
  echo "[INFO] Bridge already running with PID $(cat "$PID_FILE") on port ${CIEL_JAN_PORT}"
else
  export CIEL_JAN_PORT="$(choose_port)"
  echo "[INFO] Starting CIEL/Ω bridge on http://${CIEL_JAN_HOST}:${CIEL_JAN_PORT}"
  nohup python3 "$BUNDLE_DIR/ciel_jan_bridge/ciel_jan_bridge.py" > "$LOG_FILE" 2>&1 &
  echo $! > "$PID_FILE"
  sleep 2
  if ! kill -0 "$(cat "$PID_FILE")" 2>/dev/null; then
    echo "[ERROR] Bridge failed to stay up. Check $LOG_FILE"
    exit 1
  fi
fi

if command -v jan >/dev/null 2>&1; then
  (jan >/dev/null 2>&1 &) || true
elif [[ -x /usr/bin/jan ]]; then
  (/usr/bin/jan >/dev/null 2>&1 &) || true
elif command -v gtk-launch >/dev/null 2>&1; then
  (gtk-launch jan >/dev/null 2>&1 &) || true
else
  echo "[WARN] Could not auto-launch Jan. Start it from your app menu."
fi

cat <<EOF

CIEL/Ω bridge is running.

Use these settings in Jan:
  Name:     CIEL/Ω Local
  Base URL: http://${CIEL_JAN_HOST}:${CIEL_JAN_PORT}/v1
  API Key:  ciel-local
  Model:    ciel-omega

Bridge log: $LOG_FILE
Bridge PID: $(cat "$PID_FILE")
EOF
