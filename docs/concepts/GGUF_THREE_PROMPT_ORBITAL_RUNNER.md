# GGUF_THREE_PROMPT_ORBITAL_RUNNER

This runner stabilizes a local GGUF conversation through a three-step protocol:

1. prompt 1: exact short reply target (`READY-1`)
2. prompt 2: exact short reply target (`READY-2`)
3. final prompt: actual semantic test

The runner performs:
- orbital pre-check (`run_global_pass`)
- backend start/attach
- three-prompt session over OpenAI-compatible local API
- orbital post-check
- report export to `reports/gguf_three_prompt_orbital/`
