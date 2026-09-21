import logging
import json  
from get_path import get_project_root
from db_connection import get_connection



# Obtaining file path
base_dir = get_project_root()
log_data_path = base_dir / "logs" / "load_order.log"
proc_data_path = base_dir / "data" / "processed"
sql_path = base_dir / "sql" / "load_orders.sql"

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

# connecting to database
conn = get_connection()
cursor = conn.cursor()

# Open SQL files
with open(sql_path, "r", encoding="utf-8") as sql_file:
    sql_script = sql_file.read()


# Loop through list of files
for f in json_files:
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
                      i["quantity"],
                      i["order_total"]
                    )
                cursor.execute(sql_script,values)
                 
    except FileNotFoundError:
        logging.error(f"File not found: {f.name}")

     
conn.commit() 
cursor.close()
conn.close()