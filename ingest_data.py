import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# 1. Load credentials from .env
load_dotenv()
db_url = os.getenv("DATABASE_URL")

if not db_url:
    print("Error: DATABASE_URL not found. .env file error")
    exit()

# 2. Connect to Neon PostgreSQL using connection string
print("Connecting to Neon Database")
engine = create_engine(db_url)

# 3. Executing the SQL script to create tables
print("Creating tables and constraints")
with engine.begin() as conn:
    with open('schema.sql', 'r') as file:
        sql_script = file.read()
        conn.execute(text(sql_script))
print("Tables created successfully!")

# 4. Ingestoing the cleaned CSV data into the tables
folder_path = "Cleaned_CSV_Data"

tables_to_load = [
    'categories', 'customers', 'employees', 'shippers', 
    'suppliers', 'products', 'orders', 'ordersdetails'
]

print("\nStarting Data Ingestion...")
with engine.begin() as conn:
    for table in tables_to_load:
        csv_file = os.path.join(folder_path, f"{table}.csv")
        if os.path.exists(csv_file):
            print(f"Loading {table}.csv into database")
            df = pd.read_csv(csv_file)
            
            # 1. Lowercase all column names to match PostgreSQL
            df.columns = df.columns.str.lower()
            
            # 2. Handle specific CSV column name mismatches/typos
            if table == 'categories' and 'descriptiontext' in df.columns:
                df = df.rename(columns={'descriptiontext': 'description'})
                
            if table == 'customers' and 'contractname' in df.columns:
                df = df.rename(columns={'contractname': 'contactname'})
                
            if table == 'suppliers' and 'suppliersname' in df.columns:
                df = df.rename(columns={'suppliersname': 'suppliername'})
                

            if table == 'products' and 'suppliersid' in df.columns:
                df = df.rename(columns={'suppliersid': 'supplierid'})

            
            # Append data to the pre-existing tables created by our SQL script
            df.to_sql(table, con=conn, if_exists='append', index=False)
        else:
            print(f"Warning: {csv_file} not found.")

print("\n Infrastructure and Data Ingestion is complete.")
