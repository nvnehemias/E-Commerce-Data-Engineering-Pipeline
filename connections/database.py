from db_connection import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute("select 1;")

row = cur.fetchone()

print(row)

cur.close()
conn.close()