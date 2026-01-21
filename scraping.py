from mp_api.client import MPRester

API_KEY = "BQX0XRiA88vGwkValqBMdLw3459tJAOA"  # Replace with your personal key

# Recommended usage with the Python "with" context manager:
with MPRester(API_KEY) as mpr:
    # Example query: Get materials that include Mo and S (e.g., MoS2-like compounds)
    results = mpr.materials.summary.search(material_ids=["mp-149", "mp-13", "mp-22526"])

    # Print the first few results
    for entry in results:
        print("Material ID:", entry.material_id)
        print("Formula:", entry.formula_pretty)
