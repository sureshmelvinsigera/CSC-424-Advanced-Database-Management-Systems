import psycopg2


def delete_part(part_id):
    """delete part by part id
    :param part_id:
    :return: rows_deleted
    """
    conn = None
    rows_deleted = 0
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
        cur.execute("""DELETE FROM parts WHERE part_id = %s""", (part_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
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

    return rows_deleted


if __name__ == '__main__':
    deleted_rows = delete_part(2)
    print('The number of deleted rows: ', deleted_rows)
