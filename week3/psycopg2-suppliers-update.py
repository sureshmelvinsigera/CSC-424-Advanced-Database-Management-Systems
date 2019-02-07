import psycopg2


def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(user="postgres",
                                password="CSI1",
                                host="localhost",
                                port="5432",
                                database="suppliers")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (vendor_name, vendor_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    update_vendor(1, "3M Inc.")
