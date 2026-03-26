#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
: "${CIEL_ROOT:?Set CIEL_ROOT=/absolute/path/to/ciel_omega}"
export PYTHONUNBUFFERED=1
python3 "$SCRIPT_DIR/ciel_jan_bridge.py"
