#!/usr/bin/env bash
set -euo pipefail

BUNDLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
JAN_DEB="${JAN_DEB:-$BUNDLE_DIR/Jan_0.7.8_amd64.deb}"

if [[ -f /etc/os-release ]]; then
  . /etc/os-release
  case "${ID:-}:${ID_LIKE:-}" in
    debian:*|ubuntu:*|linuxmint:*|pop:*|*:*debian*|*:*ubuntu*) ;;
    *)
      echo "[WARN] This script targets Debian/Ubuntu-family systems. Detected: ${PRETTY_NAME:-unknown}"
      ;;
  esac
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "[ERROR] python3 is required."
  exit 1
fi

if [[ ! -f "$JAN_DEB" ]]; then
  echo "[ERROR] Bundled Jan .deb not found: $JAN_DEB"
  echo "        Set JAN_DEB=/path/to/Jan_0.7.8_amd64.deb if you moved it."
  exit 1
fi

pushd "$(dirname "$JAN_DEB")" >/dev/null
  echo "[INFO] Installing bundled Jan package: $(basename "$JAN_DEB")"
  sudo apt-get install -y ./$(basename "$JAN_DEB")
popd >/dev/null

echo "[OK] Jan installed."
