import os
import sys 
import psycopg
from pathlib import Path
import logging
from dotenv import load_dotenv

# Importing get_project_root function
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0,str(project_root/"src"))
from ecommerce_pipeline.get_path import get_project_root

# getting path
base_dir = get_project_root()
log_data_path = base_dir / "logs" / "sql.log"

# creating log format
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
def get_connection():

    load_dotenv()

    try:
        logging.info("Starting database connection")
        connection = psycopg.connect(
            host = os.getenv("DB_HOST","127.0.0.1"),
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            port = os.getenv("DB_PORT","5432")
        )
        logging.info("Successfully connected to the database!")
        
    except psycopg.Error as e:
        logging.error(f"Error connecting to PostgreSQL: {e}")

    return connection