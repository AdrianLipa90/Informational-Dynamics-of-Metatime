#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List

DEFAULT_HOST = os.environ.get("CIEL_JAN_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.environ.get("CIEL_JAN_PORT", "8080"))
MODEL_ID = os.environ.get("CIEL_JAN_MODEL_ID", "ciel-omega")

CIEL_ROOT = os.environ.get("CIEL_ROOT")
if not CIEL_ROOT:
    # fallback: assume this script may live next to the repo or inside it
    here = Path(__file__).resolve().parent
    candidates = [
        here / "ciel_omega",
        here.parent / "ciel_omega",
        Path.cwd() / "ciel_omega",
        Path.cwd(),
    ]
    for c in candidates:
        if (c / "ciel_orchestrator.py").exists() or (c / "ciel_omega" / "ciel_orchestrator.py").exists():
            CIEL_ROOT = str(c if (c / "ciel_orchestrator.py").exists() else (c / "ciel_omega"))
            break

if not CIEL_ROOT:
    raise RuntimeError(
        "Cannot locate CIEL root. Set environment variable CIEL_ROOT=/absolute/path/to/ciel_omega"
    )

if CIEL_ROOT not in sys.path:
    sys.path.insert(0, CIEL_ROOT)

from ciel_client import CIELClient  # type: ignore


def _safe_text_response(text: str, result: Dict[str, Any]) -> str:
    state = result.get("ciel_result", {}).get("ciel_state", {})
    mood = state.get("mood")
    dom = state.get("dominant_emotion")
    soul = result.get("ciel_result", {}).get("soul_measure")
    ethics = result.get("ciel_result", {}).get("ethics_passed")
    lines = [
        f"CIEL/Ω analysis for: {text}",
        f"dominant_emotion={dom}",
        f"mood={mood}",
        f"soul_measure={soul}",
        f"ethics_passed={ethics}",
    ]
    return "\n".join(lines)


class _State:
    client: CIELClient | None = None
    model_path: str | None = os.environ.get("CIEL_GGUF_MODEL") or None


def get_client() -> CIELClient:
    if _State.client is None:
        _State.client = CIELClient(model_path=_State.model_path)
    return _State.client


def extract_user_text(messages: List[Dict[str, Any]]) -> str:
    user_messages = [m for m in messages if m.get("role") == "user"]
    if not user_messages:
        return ""
    last = user_messages[-1].get("content", "")
    if isinstance(last, str):
        return last
    if isinstance(last, list):
        parts = []
        for item in last:
            if isinstance(item, dict) and item.get("type") in ("text", "input_text"):
                parts.append(item.get("text", ""))
        return "\n".join(p for p in parts if p)
    return str(last)


def count_tokens_rough(text: str) -> int:
    return max(1, len(text.split())) if text else 0


class JanBridgeHandler(BaseHTTPRequestHandler):
    server_version = "CIELJanBridge/0.1"

    def _send_json(self, code: int, payload: Dict[str, Any]) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def _send_sse(self, chunks: List[str], model: str, completion_id: str, created: int) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        for i, chunk in enumerate(chunks):
            payload = {
                "id": completion_id,
                "object": "chat.completion.chunk",
                "created": created,
                "model": model,
                "choices": [{
                    "index": 0,
                    "delta": {"content": chunk} if chunk else {},
                    "finish_reason": None,
                }],
            }
            self.wfile.write(f"data: {json.dumps(payload, ensure_ascii=False)}\n\n".encode("utf-8"))
            self.wfile.flush()
        done_payload = {
            "id": completion_id,
            "object": "chat.completion.chunk",
            "created": created,
            "model": model,
            "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
        }
        self.wfile.write(f"data: {json.dumps(done_payload, ensure_ascii=False)}\n\n".encode("utf-8"))
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        if self.path in ("/health", "/healthz"):
            self._send_json(200, {"ok": True, "service": "ciel-jan-bridge"})
            return
        if self.path == "/v1/models":
            self._send_json(200, {
                "object": "list",
                "data": [{
                    "id": MODEL_ID,
                    "object": "model",
                    "created": int(time.time()),
                    "owned_by": "local",
                }],
            })
            return
        self._send_json(404, {"error": {"message": f"Unknown path: {self.path}"}})

    def do_POST(self):
        if self.path != "/v1/chat/completions":
            self._send_json(404, {"error": {"message": f"Unknown path: {self.path}"}})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length) if length else b"{}"
            req = json.loads(raw.decode("utf-8"))
        except Exception as e:
            self._send_json(400, {"error": {"message": f"Invalid JSON: {e}"}})
            return

        model = req.get("model", MODEL_ID)
        messages = req.get("messages", [])
        stream = bool(req.get("stream", False))
        text = extract_user_text(messages)
        if not text:
            self._send_json(400, {"error": {"message": "No user message found"}})
            return

        try:
            client = get_client()
            result = client.process(text, use_llm=True, verbose=False)
            answer = result.get("llm_response") or _safe_text_response(text, result)
        except Exception as e:
            self._send_json(500, {"error": {"message": f"CIEL processing error: {e}"}})
            return

        completion_id = f"chatcmpl-{uuid.uuid4().hex[:24]}"
        created = int(time.time())
        usage = {
            "prompt_tokens": count_tokens_rough(text),
            "completion_tokens": count_tokens_rough(answer),
            "total_tokens": count_tokens_rough(text) + count_tokens_rough(answer),
        }

        if stream:
            step = 64
            chunks = [answer[i:i+step] for i in range(0, len(answer), step)] or [""]
            self._send_sse(chunks, model, completion_id, created)
            return

        self._send_json(200, {
            "id": completion_id,
            "object": "chat.completion",
            "created": created,
            "model": model,
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": answer},
                "finish_reason": "stop",
            }],
            "usage": usage,
        })


def main() -> None:
    httpd = ThreadingHTTPServer((DEFAULT_HOST, DEFAULT_PORT), JanBridgeHandler)
    print(f"CIEL/Ω Jan bridge listening on http://{DEFAULT_HOST}:{DEFAULT_PORT}")
    print(f"CIEL root: {CIEL_ROOT}")
    if _State.model_path:
        print(f"GGUF model: {_State.model_path}")
    else:
        print("GGUF model: none (bridge will return structured CIEL output if no backend is available)")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
