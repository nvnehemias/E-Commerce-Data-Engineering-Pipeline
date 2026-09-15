import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

try:
    connection = psycopg.connect(
        host = os.getenv("DB_HOST","127.0.0.1"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT","5432")
    )

    print("Successfully connected to the database!")

except psycopg.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")