import pandas as pd
import os

file_path = "Global Online Orders/orders_frostonline.xlsx"
output_folder = "Cleaned_CSV_Data"

# a folder to store the cleaned CSVs
os.makedirs(output_folder, exist_ok=True)

print("Starting Data Cleaning & Export")

# Load all sheets
dataframes = pd.read_excel(file_path, sheet_name=None)

# 1. Clean the 'customers' table
if 'customers' in dataframes:
    print("Cleaning 'customers' table: Filling missing PostalCode with 'UNKNOWN'...")
    # Filled the missing postal code with a placeholder
    dataframes['customers']['PostalCode'].fillna('UNKNOWN', inplace=True)

# 2. Exporting all tables to individual CSVs
for table_name, df in dataframes.items():
    csv_filename = os.path.join(output_folder, f"{table_name}.csv")
    
    # Exportong to CSV without the index column
    df.to_csv(csv_filename, index=False)
    print(f"Exported: {csv_filename}")

print("\n All cleaned data is saved as CSV files in the Cleaned_CSV_Data folder")