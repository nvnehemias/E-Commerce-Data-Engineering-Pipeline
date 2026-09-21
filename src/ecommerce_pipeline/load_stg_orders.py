import logging
import json  
from get_path import get_project_root
from db_connection import get_connection


# Obtaining file path
base_dir = get_project_root()
log_stg_data_path = base_dir / "logs" / "load_stg_orders.log"
raw_data_path = base_dir / "data" / "raw"
sql_stg_path = base_dir / "sql" / "load_stg_orders.sql"


# Finding all files with .json 
raw_json_files = list(raw_data_path.glob("*.json"))

# Logging Basic Config
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    handlers = [
        logging.FileHandler(log_stg_data_path, encoding = "utf-8"),
        logging.StreamHandler()
    ],
    force = True
)

# First logging
logging.info("Starting process to load staging orders.")

# connecting to database
conn = get_connection()
cursor = conn.cursor()

# Open SQL files
with open(sql_stg_path, "r", encoding="utf-8") as sql_stg_file:
    sql_stg_script = sql_stg_file.read()


# Loop through list of files
for f in raw_json_files:
    logging.info(f"Loading file: {f.name}")

    try: 
        with open(f,"r",encoding = 'utf-8') as file:
            # Loading file
            data = json.load(file)    
            logging.info(f"Successfully loaded {f.name}.")
            
            # Looping through values
            for i in data:
                values = (
                      i["order_id"],
                      i["customer_id"],
                      i["product"],
                      i["price"],
                      i["quantity"]
                    )
                cursor.execute(sql_stg_script,values)
                 
    except FileNotFoundError:
        logging.error(f"File not found: {f.name}")

     
conn.commit() 
cursor.close()
conn.close()