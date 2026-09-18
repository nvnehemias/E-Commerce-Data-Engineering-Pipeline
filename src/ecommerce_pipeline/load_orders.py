import logging
import json  
from pathlib import Path
from get_path import get_project_root
from db_connection import get_connection



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

# connecting to database
conn = get_connection()
cursor = conn.cursor()

# Loop through list of files
for f in json_files:
    logging.info(f"Loading file: {f.name}")

    try: 
        with open(f,"r",encoding = 'utf-8') as file:
            # Loading file
            data = json.load(file)    
            logging.info(f"Successfully loaded {f.name}.")
            sql_statement = """
                            insert into orders (order_id, customer_id, product, price, quantity, order_total)
                            values (%s,%s,%s,%s,%s,%s)
                            on conflict (order_id) do nothing;
                            """
            for i in data:
                 values = (
                      i["order_id"],
                      i["customer_id"],
                      i["product"],
                      i["price"],
                      i["quantity"],
                      i["order_total"]
                      )
                 cursor.execute(sql_statement,values)
                 
    except FileNotFoundError:
            logging.error(f"File not found: {f.name}")

     
conn.commit() 
cursor.close()
conn.close()