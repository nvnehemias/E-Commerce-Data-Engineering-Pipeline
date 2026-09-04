import logging
from convert_order import convert_order
from get_path import get_project_root
from pathlib import Path
import json 
import os 


# Obtaining file path
base_dir = get_project_root()
log_data_path = base_dir / "logs" / "pipeline.log"
raw_data_path = base_dir / "data" / "raw"
proc_data_path = base_dir / "data" / "processed" / "cleaned_"


# Finding all files with .json 
json_files = list(raw_data_path.glob("**/*.json"))


# Logging Basic Config
logging.basicConfig(
    # filename = log_data_path,
    # filemode = "a",
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
logging.info("Starting pipeline")


# Looping through all files and loading data
for file_path in json_files:

    # Printing and writing logging info
    logging.info(f"Loading file: {file_path.name}")

    with open(file_path,"r",encoding = 'utf-8') as file:

        try: 
            data = json.load(file)
        except:
             logging.error(f"Failed to load file: {file_path.name}")
             continue

        # Passing data to function
        cleaned_orders, report = convert_order(data)

        # Logging total orders processed
        p_o_value = report.get("total_orders",0)
        logging.info(f"Processing {p_o_value} orders")

        
        
        
    with open(f"{proc_data_path}{file_path.name}","w", encoding = "utf-8") as file:
        json.dump(cleaned_orders, file, indent = 4)

    if report.get("missing_customers",0) > 0:
        m_o_value = report.get("missing_customers",0)
        logging.warning(f"Total missing customers: {m_o_value}")

    if report.get("invalid_price",0) > 0:
        i_p_value = report.get("invalid_price",0)
        logging.warning(f"Total orders with invalid price {i_p_value}")

    if report.get("invalid_quantity",0) > 0:
            i_q_value = report.get("invalid_quantity",0)
            logging.warning(f"Total orders with invalid quantity: {i_q_value}")

    if report.get("duplicate_orders",0) > 0:
                i_q_value = report.get("duplicate_orders",0)
                logging.warning(f"Total duplicate orders found: {i_q_value}")

    if report.get("successful_orders",0) > 0: 
        s_o_value = report.get("successful_orders",0)
        logging.info(f"Successfully processed {s_o_value} orders")

        

    logging.info(f"Finished processing: {file_path.name}")
