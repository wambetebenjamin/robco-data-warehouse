import pandas as pd

# Load data
suppliers = pd.read_json('../data/suppliers.json')
inventory = pd.read_csv('../data/inventory.csv')

# Merge suppliers and inventory
merged_data = inventory.merge(suppliers, on="supplier_id", how="left")
print("Transformed Data:\n", merged_data)
