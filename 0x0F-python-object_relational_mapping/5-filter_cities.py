#!/usr/bin/python3
"""Takes in a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
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
    result: str = """SELECT c.id, c.name, s.name
    FROM cities AS c
    Join states AS s
    ON c.state_id = s.id
    HAVING BINARY s.name = %s
    ORDER BY c.id;"""

    database = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=database_name,
    )
    cursor = database.cursor()

    cursor.execute(result, (argument,))
    rows = cursor.fetchall()
    cities = tuple(row[1] for row in rows)
    cities = ', '.join(cities)
    print(cities)
