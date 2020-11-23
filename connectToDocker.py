from psycopg2 import connect

# table_create = """CREATE TABLE IF NOT EXISTS films (
#     title       varchar(40)
# );"""
#
# table_insert = "INSERT INTO films VALUES ('Logan');"

table_select = "SELECT * FROM films;"

# declare connection instance
conn = connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="postgres")

# declare a cursor object from the connection
cursor = conn.cursor()

# execute an SQL statement using the psycopg2 cursor object
# cursor.execute(f"{table_create}")
# cursor.execute(f"{table_insert}")
# conn.commit()
cursor.execute(f"{table_select}")

records = cursor.fetchall()
for record in records:
    print(record)

# # enumerate() over the PostgreSQL records

# close the cursor object to avoid memory leaks
cursor.close()

# close the connection as well
conn.close()
