import psycopg2


def insert_vendor_list(vendor_list):
    """ insert multiple vendors into the vendors table  """
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(user="postgres",
                                password="CSI1",
                                host="localhost",
                                port="5432",
                                database="suppliers")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    vendors = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]
    insert_vendor_list(vendors)
