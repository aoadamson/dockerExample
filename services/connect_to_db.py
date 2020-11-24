from psycopg2 import connect


def connect_to_db(host, database, user, password):
    conn = connect(
        host=host,
        database=database,
        user=user,
        password=password)
    return conn