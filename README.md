# Inverse Design of 2D Heterostructures

## todo

## Encodable Properties
Material identity/composition of each layer (e.g., graphene, MoS₂, h-BN, etc.)

Stacking order (which layer comes first, second, etc.)

Twist angle between adjacent layers

Lateral offset (how much one layer is shifted sideways relative to the next)

Interlayer distance (vertical separation between layers)

Number of layers

Lattice parameters (a, b, c for each layer if relevant)

Elemental statistics (average atomic number, electronegativity for each layer)

Symmetry/space group (optional: encoded as one-hot or categorical values)

Presence/absence of defects or dopants (if your dataset includes such detail)

Stoichiometry for each layer

Layer composition/type: The identity of each monolayer (e.g., graphene, MoS₂, h-BN).

Order of stacking: Which layers come first, second, etc.

Twist angle: The relative rotation between two adjacent layers.

Lateral offset: The shift (in the x/y plane) between adjacent layers’ atomic lattices.

Interlayer spacing: Distance between adjacent monolayers.

Stacking type: AA, AB, or other categorical stacking catalogs.

Lattice constants/parameters of each layer.

Average atomic properties: Mean atomic number, electronegativity, etc., for each layer or the full stack.

Number of layers