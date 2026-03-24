from __future__ import annotations
from pathlib import Path
import json, os, sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SYS_ROOT = REPO_ROOT / "systems" / "CIEL_OMEGA_COMPLETE_SYSTEM"
if str(SYS_ROOT) not in sys.path:
    sys.path.insert(0, str(SYS_ROOT))

from ciel_omega.inference.gguf_backend import GGUFBackendConfig, GGUFBackendRunner
from ciel_omega.inference.middleware import run_three_prompt_session
from ciel_omega.orbital.global_pass import run_global_pass

PORT = int(os.environ.get("GGUF_PORT", "18080"))
LLAMA_SERVER = os.environ.get("LLAMA_SERVER_PATH", "/mnt/data/llama_bin/build/bin/llama-server")
MODEL_PATH = os.environ.get("GGUF_MODEL_PATH", "/mnt/data/qwen2.5-0.5b-instruct-q2_k.gguf")
FINAL_PROMPT = os.environ.get("GGUF_FINAL_PROMPT", "In one short sentence, say whether orbital semantics is active.")


def main() -> None:
    out_dir = REPO_ROOT / "reports" / "gguf_three_prompt_orbital"
    out_dir.mkdir(parents=True, exist_ok=True)

    pre = run_global_pass()
    (out_dir / "orbital_pre.json").write_text(json.dumps(pre, indent=2), encoding="utf-8")

    cfg = GGUFBackendConfig(
        llama_server_path=LLAMA_SERVER,
        model_path=MODEL_PATH,
        port=PORT,
        ctx_size=1024,
        ngl=0,
        no_warmup=True,
    )
    runner = GGUFBackendRunner(cfg)

    attached = runner.is_alive()
    if not attached:
        runner.start(out_dir / "llama_server.log")
        ready = runner.wait_until_ready(timeout_s=180)
        if not ready:
            raise RuntimeError("GGUF backend failed to become ready")
    else:
        (out_dir / "llama_server.log").write_text("Attached to existing backend\n", encoding="utf-8")

    models = runner.list_models()
    (out_dir / "models.json").write_text(json.dumps(models, indent=2), encoding="utf-8")
    model_name = models["data"][0]["id"] if models.get("data") else Path(MODEL_PATH).name

    session = run_three_prompt_session(runner, model=model_name, final_prompt=FINAL_PROMPT, temperature=0.0)
    (out_dir / "session.json").write_text(json.dumps(session, indent=2), encoding="utf-8")

    post = run_global_pass()
    (out_dir / "orbital_post.json").write_text(json.dumps(post, indent=2), encoding="utf-8")

    md = ["# GGUF Three-Prompt Orbital Run", "", f"- attached_to_existing_backend: {attached}", f"- model: `{model_name}`", "", "## Steps"]
    for i, step in enumerate(session["steps"], start=1):
        md += [f"### Step {i}", f"- prompt: `{step['prompt']}`", f"- response: `{step['response']}`", ""]
    md += ["## Orbital Metrics Pre", ""]
    for k, v in pre["final"].items():
        md.append(f"- {k}: {v}")
    md += ["", "## Orbital Metrics Post", ""]
    for k, v in post["final"].items():
        md.append(f"- {k}: {v}")
    (out_dir / "summary.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps({
        "attached": attached,
        "model": model_name,
        "final_text": session["final_text"],
        "step_responses": [s["response"] for s in session["steps"]],
        "pre_final": pre["final"],
        "post_final": post["final"],
    }, indent=2))

if __name__ == "__main__":
    main()
