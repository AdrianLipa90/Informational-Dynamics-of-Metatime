from __future__ import annotations
from typing import Any

STABILIZATION_MESSAGES = [
    {"role": "user", "content": "Reply with exactly: READY-1"},
    {"role": "user", "content": "Reply with exactly: READY-2"},
]

def extract_text(response: dict[str, Any]) -> str:
    try:
        return response["choices"][0]["message"]["content"]
    except Exception:
        return "<unparsed>"


def run_three_prompt_session(runner, model: str, final_prompt: str, temperature: float = 0.0) -> dict[str, Any]:
    transcript: list[dict[str, str]] = [
        {
            "role": "system",
            "content": "You are a local GGUF test model. Follow the requested reply format exactly when possible.",
        }
    ]
    steps: list[dict[str, Any]] = []
    for msg in STABILIZATION_MESSAGES:
        transcript.append(msg)
        resp = runner.chat(model=model, messages=transcript, temperature=temperature, max_tokens=24)
        text = extract_text(resp)
        transcript.append({"role": "assistant", "content": text})
        steps.append({"prompt": msg["content"], "response": text, "raw": resp})
    final_msg = {"role": "user", "content": final_prompt}
    transcript.append(final_msg)
    final_resp = runner.chat(model=model, messages=transcript, temperature=temperature, max_tokens=96)
    final_text = extract_text(final_resp)
    transcript.append({"role": "assistant", "content": final_text})
    steps.append({"prompt": final_prompt, "response": final_text, "raw": final_resp})
    return {"transcript": transcript, "steps": steps, "final_text": final_text}
