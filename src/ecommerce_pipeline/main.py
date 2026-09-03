from convert_order import convert_order
from get_path import get_project_root
from pathlib import Path
import logging
import json 
import os 


# Obtaining file path
# base_dir = Path(__file__).parent
base_dir = get_project_root()
raw_data_path = base_dir / "data" / "raw"
proc_data_path = base_dir / "data" / "processed" / "cleaned_"

# Finding all files with .json 
json_files = list(raw_data_path.glob("**/**/*.json"))
print(base_dir)
print(raw_data_path)
print(json_files)
# Looping through all files and loading data
for file_path in json_files:
    print(f"Loading file: {file_path.name}")
    with open(file_path,"r",encoding = 'utf-8') as file:
        data = json.load(file)

        cleaned_orders, report = convert_order(data)
        print(report)
        
    with open(f"{proc_data_path}{file_path.name}","w", encoding = "utf-8") as file:
        json.dump(cleaned_orders, file, indent = 4)

