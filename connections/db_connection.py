import psycopg

try:
        
    connection = psycopg.connect(
        host = "127.0.0.1",
        dbname= "ecommerce_pipeline",
        user="postgres",
        password="Gibson1paul",
        port="5432"
    )

    print("Successfully connected to the database!")

except psycopg.Error as e:
    print(f"Error connecting to PostgreSQL{e}")