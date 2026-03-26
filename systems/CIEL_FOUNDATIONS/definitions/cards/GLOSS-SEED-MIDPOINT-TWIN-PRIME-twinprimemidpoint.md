# TwinPrimeMidpoint - TwinPrimeMidpoint

| field | value |
|---|---|
| stable_id | `GLOSS-SEED-MIDPOINT-TWIN-PRIME` |
| canonical_id | `seed.midpoint.twin_prime` |
| card_type | `seed` |
| class | `seed` |
| subclass | `midpoint` |
| status | `canonical_record` |
| certainty_scope | `canonical_ontology_record` |
| units | `see card / symbolic` |
| value | `` |

## Description
relational midpoint seed between twin primes

## Formal definition
```text
S(p,p+2)=p+1
```

## Tags
`type:seed`, `domain:omega`, `status:canonical_record`, `role:relational`, `layer:runtime`, `bind:registry`, `domain:metatime`

## Relational couplings
| relation | targets |
|---|---|
| `seeds` | `trajectory` |
| `projects_to` | `collatz` |
| `stabilizes` | `midpoint_seed` |

## Cross references
- `trajectory`
- `collatz`
- `attractor`
- `seeds`
- `projects_to`
- `stabilizes`

## Source-of-truth anchors
- `systems/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/vocabulary.yaml`

## Runtime binding
```yaml
module: ciel_omega.core.braid.defaults
function: twin_prime_midpoint
mode: deferred
```

## Notes
creates central seed between two prime boundaries
