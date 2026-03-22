import pandas as pd
import os

# excel file
file_path = "Global Online Orders/orders_frostonline.xlsx"

print("Starting Data Exploration")

if os.path.exists(file_path):
    print(f"Found {file_path}! Loading all sheets...")
    
    # using sheet_name=None loads ALL sheets into a dictionary of DataFrames
    dataframes = pd.read_excel(file_path, sheet_name=None)
    
    # Loop through each sheet and inspect it
    for table_name, df in dataframes.items():
        print(f"\n--- Table (Sheet): {table_name} ---")
        print(f"Shape: {df.shape}")
        
        # Check for missing values
        missing_values = df.isnull().sum()
        missing_values = missing_values[missing_values > 0]
        
        if not missing_values.empty:
            print("Missing Values Found:")
            print(missing_values)
        else:
            print("No missing values detected.")
            
    # Preview the 'orders' table 
    if 'orders' in dataframes:
        print("\n Preview of 'orders' Table")
        print(dataframes['orders'].head())
else:
    print(f"Error: Could not find {file_path}.")