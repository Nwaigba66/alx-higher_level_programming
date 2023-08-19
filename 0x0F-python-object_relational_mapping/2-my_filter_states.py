#!/usr/bin/python3
"""Lists all states with a name starting with `N` from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    database_name: str = sys.argv[3]
    argument: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306
    result: str = """SELECT * FROM states WHERE name = '{}' ORDER BY id""".format(argument)

    database = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=database_name,
    )
    cursor = database.cursor()

    cursor.execute(result)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
