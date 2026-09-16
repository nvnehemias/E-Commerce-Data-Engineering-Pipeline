import logging
from get_path import get_project_root
from pathlib import Path
import json 
import os 

# Obtaining file path
base_dir = get_project_root()
log_data_path = base_dir / "logs" / "load_order.log"
proc_data_path = base_dir / "data" / "processed"

# Finding all files with .json 
json_files = list(proc_data_path.glob("cleaned_*.json"))

# Logging Basic Config
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler(log_data_path, encoding = "utf-8"),
        logging.StreamHandler()
    ],
    force = True
)

# First logging
logging.info("Starting process to load orders.")

# Loop through list of files
for f in json_files:
    logging.info(f"Loading file: {f.name}")

    try: 
        with open(f,"r",encoding = 'utf-8') as file:
            # Loading file
            data = json.load(file)    
            logging.info(f"Successfully loaded {f.name}.")
    except FileNotFoundError:
            logging.error(f"File not found: {f.name}")


    return data 