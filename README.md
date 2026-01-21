# Inverse Design of 2D Heterostructures


## goal

?? determine predictive qualities of a good semiconductor using the materials we know that work well and the ones that don't work well

have a gvae (graph variational autoencoder) that randomly generates 2d heterostructures

have a gnn that is used to predict features of the structure

use gnn and gvae to mass generate structures and verify the ones using quantumespresso that have good values from the gnn

## plan
1. Clustering Model to find the properties that affect features such as band gap range, carrier mobility, binding energy (good for semicond use) the most.
2. Use Graph Variational Auto-Encoder to generate possible 2D Heterostructures.
3. Use Graph Neural Network to test the properties of such structures and then determine if they are within viable range.
4. For ones with exceptional results, use Quantum Espresso to run Density Functional Theory on them to verify results.

### Encodable Properties
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

### data
https://next-gen.materialsproject.org/materials/