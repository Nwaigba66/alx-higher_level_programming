#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    database_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306
    result: str = """SELECT * FROM cities ORDER BY id"""

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
