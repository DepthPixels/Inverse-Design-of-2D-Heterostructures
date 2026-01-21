from mp_api.client import MPRester

API_KEY = "BQX0XRiA88vGwkValqBMdLw3459tJAOA"  # Replace with your personal key

# Recommended usage with the Python "with" context manager:
with MPRester(API_KEY) as mpr:
    # Example query: Get materials that include Mo and S (e.g., MoS2-like compounds)
    results = mpr.materials.summary.search(elements=["Mo", "S"], n_elements=2, crystal_system="hexagonal", band_gap_min=0)

    # Print the first few results
    for entry in results[:5]:
        print("Material ID:", entry.material_id)
        print("Formula:", entry.formula_pretty)
        print("Band gap:", entry.band_gap)
        print("Lattice:", entry.lattice)
        print("Crystal System:", entry.crystal_system)
        print("---")
