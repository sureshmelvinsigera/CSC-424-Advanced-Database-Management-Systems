import psycopg2

connection = None

try:
    connection = psycopg2.connect(user="postgres",
                                  password="CSI1",
                                  host="localhost",
                                  port="5432",
                                  database="dvd")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")
