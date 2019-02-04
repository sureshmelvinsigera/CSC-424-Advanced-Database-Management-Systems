import psycopg2

# create the to the connection database via psycopg2.connect
connection = psycopg2.connect(
    database='sample',
    user='postgres',
    password='CSI1',
    host='localhost',
    port='5432'
)

# print out the connection information
print(connection)
