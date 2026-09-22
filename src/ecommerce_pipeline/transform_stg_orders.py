import logging
import json  
from get_path import get_project_root
from db_connection import get_connection


# Obtaining file path
base_dir = get_project_root()
log_stg_order_path = base_dir / "logs" / "transform_stg_orders.log"
# raw_data_path = base_dir / "data" / "raw"
sql_stg_path = base_dir / "sql" / "load_stg_orders.sql"


# Finding all files with .json 
# raw_json_files = list(raw_data_path.glob("*.json"))

# Logging Basic Config
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler(log_stg_order_path, encoding = "utf-8"),
        logging.StreamHandler()
    ],
    force = True
)

# First logging
logging.info("Starting process to transform staging orders.")