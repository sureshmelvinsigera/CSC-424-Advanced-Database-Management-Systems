import psycopg2

# create the to the connection database via psycopg2.connect
connection = psycopg2.connect(
    database='sample',
    user='postgres',
    password='CSI1',
    host='localhost',
    port='5432'
)

cur = connection.cursor()
cur.execute(
    '''
    CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);
    '''
)
print("Table created successfully")
connection.commit()  # apply the changes
connection.close()  # close the connection
