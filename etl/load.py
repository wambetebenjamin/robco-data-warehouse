import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('postgresql://postgres:password@localhost:5432/robco_datawarehouse')

# Load transformed data
merged_data = pd.read_csv('../data/inventory.csv')
merged_data.to_sql('inventory', engine, if_exists='replace', index=False)
print("Data successfully loaded into PostgreSQL!")
