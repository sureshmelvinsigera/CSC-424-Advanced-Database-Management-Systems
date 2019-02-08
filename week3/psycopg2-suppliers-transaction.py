import psycopg2


def add_part(part_name, vendor_list):
    """ Add new part and assign a vendor
    :param part_name:
    :param vendor_list:
    :return: None
    """
    # statement for inserting a new row into the parts table
    insert_part = """INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id;"""

    # statement for inserting a new row into the vendor_parts table
    assign_vendor = """INSERT INTO vendor_parts(vendor_id,part_id) VALUES(%s,%s)"""

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
        # insert a new part
        cur.execute(insert_part, (part_name,))
        # get the part id
        part_id = cur.fetchone()[0]
        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cur.execute(assign_vendor, (vendor_id, part_id))

        # close communication with the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        conn.rollback()
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 7))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))
