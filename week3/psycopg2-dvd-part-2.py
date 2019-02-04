import psycopg2
import sys

connection = None
cursor = None

try:
    connection = psycopg2.connect(user="postgres",
                                  password="CSI1",
                                  host="localhost",
                                  port="5432",
                                  database="dvd")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM actor)

    while True:
        record = cursor.fetchone()
        if record is None:
            break
        else:
            # print id, first name, and last name
            print(record[0], ' ', record[1], ' ', record[2])

except psycopg2.DatabaseError as e:
    print(e)
    if connection:
        connection.rollback()
        # exit to the system
        sys.exit(1)

finally:
    if connection:
        # close the connection
        connection.close()
