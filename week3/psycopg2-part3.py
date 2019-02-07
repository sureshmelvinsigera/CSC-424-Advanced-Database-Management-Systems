# import Python PostgreSQL DB API
import psycopg2

conn = None
cur = None
# try to connect to the DB
try:
    conn = psycopg2.connect(
        user="postgres",
        password="CSI1",
        host="localhost",
        port="5432",
        database="postgres"
    )
    cur = conn.cursor()
    # execute 1st statement
    # cur.execute(statement_1)
    # execute 2nd statement
    # cur.execute(statement_1)

    # commit the transaction
    conn.commit()

    # close the database communication
    cur.close()
# accept the error
except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        print(conn)
        conn.close()
