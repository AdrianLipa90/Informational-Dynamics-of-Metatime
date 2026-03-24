# Public Config Layer

This directory mirrors the value-bearing top-level `configs/` layer from the public `Informational-Dynamics-of-Metatime` repository and keeps the runtime-relevant files in canonical packaging position.

Included files:
- heuristics_self.json
- heuristics_user.json
- rules_immutable.json
- relational_contract.yaml
- relational_contract.py

The same relational contract pair is also mirrored into `ciel_omega/configs/` so the runtime tree can import it without depending on top-level packaging.
