# RELATIONAL_LAGRANGIAN_V62

v6.2 replaces ad hoc additions with a single effective relational potential:

\[
V_{rel}^{total} = \kappa_H R_H + \lambda_t T_{glob} + \lambda_d \Pi_{closure} + \lambda_\zeta V_{tetra}
\]

Derived from this potential:
- sector spin from the angular gradient,
- homology leak from the radial gradient,
- Poincare-disk dynamics from radial updates,
- zeta pole as a tetrahedral frame coupled through the same total potential.

This is the first version in which spin, leak, and disk dynamics are treated as projections of one generator rather than as separate ad hoc forces.
