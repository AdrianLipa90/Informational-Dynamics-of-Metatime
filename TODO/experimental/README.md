# Experimental candidates kept outside runtime

This folder stores code fragments that may be valuable for the architecture
but are not part of the validated runtime kernel.

## introspective_state_demo.py
Kept because it contains useful ideas for a future observer/debug layer:
- multichannel internal state,
- full state history / trace buffer,
- timestamped journaling,
- separation of persistent intention and transient impulse,
- quick visual diagnostics.

Not part of runtime memory channels. Treat as experimental material only.
