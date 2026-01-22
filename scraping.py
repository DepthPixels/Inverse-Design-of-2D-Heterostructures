from mp_api.client import MPRester
import os

API_KEY = os.getenv("API_KEY")  # Replace with your personal key

# Recommended usage with the Python "with" context manager:
with MPRester(API_KEY) as mpr:
    # Example query: Get materials that include Mo and S (e.g., MoS2-like compounds)
    results = mpr.materials.summary.search(material_ids=["mp-149", "mp-13", "mp-22526"])
    
    list_of_available_fields = mpr.materials.summary.available_fields
    
    print("Available Fields: ", list_of_available_fields)

    # Print the first few results
    for entry in results:
        print("Material ID:", entry.material_id)
        print("Formula:", entry.formula_pretty)