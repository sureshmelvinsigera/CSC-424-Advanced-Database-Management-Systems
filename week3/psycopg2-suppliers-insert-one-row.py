import psycopg2


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table
    :param vendor_name:
    :return: vendor_id
    """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
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
        cur.execute(sql, (vendor_name,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id


if __name__ == '__main__':
    insert_vendor("3M Co.")