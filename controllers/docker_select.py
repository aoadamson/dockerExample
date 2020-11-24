from services.connect_to_db import connect_to_db

def dockerSelect():
    table_select = "SELECT * FROM films;"

    names = []
    # declare connection instance
    conn = connect_to_db("localhost", "testdb", "postgres", "postgres")

    # declare a cursor object from the connection
    cursor = conn.cursor()

    cursor.execute(f"{table_select}")

    records = cursor.fetchall()
    for record in records:
        names.append(record)

    # close the cursor object to avoid memory leaks
    cursor.close()

    # close the connection as well
    conn.close()

    return names
