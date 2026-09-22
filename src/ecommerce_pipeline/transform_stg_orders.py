import logging
import json  
from get_path import get_project_root
from db_connection import get_connection


# Obtaining file path
base_dir = get_project_root()
log_stg_order_path = base_dir / "logs" / "transform_stg_orders.log"
sql_trans_stg_path = base_dir / "sql" / "transform_stg_orders.sql"


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

# connecting to database
conn = get_connection()
cursor = conn.cursor()
logging.info("Connecting to database.")

# Opening sql file 
with open(sql_trans_stg_path,"r", encoding = "utf-8") as file:
    sql_script = file.read()

cursor.execute(sql_script)
logging.info("Executing sql command.")

# Commiting and closing connection
conn.commit() 
cursor.close()
conn.close()
logging.info("Closing connection to database.")