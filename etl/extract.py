import pandas as pd

# Load JSON data
suppliers = pd.read_json('../data/suppliers.json')
print("Suppliers Data:\n", suppliers)

# Load CSV data
inventory = pd.read_csv('../data/inventory.csv')
print("Inventory Data:\n", inventory)
