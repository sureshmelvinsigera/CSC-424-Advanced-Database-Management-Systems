import psycopg2

# Connect to the PostgreSQL database

conn = psycopg2.connect("dbname=testdb user=postgres password='CSI1'")

print(conn)