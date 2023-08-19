#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

"""Main Execution Block
"""
if __name__ == "__main__":
  # Retrieve command-line arguments (username, password, and database name)
  username: str = sys.argv[1]
  password: str = sys.argv[2]
  database_name: str = sys.argv[3]
  host: str = "localhost"
  port: int = 3306
  result: str = """SELECT * FROM states ORDER BY id"""

"""Database Connection
"""
database = MySQLdb.connect(
  user=username,
  host=host,
  port=port,
  password=password,
  database=database_name,
)
cursor = database.cursor()

cursor.execute(result)
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
cursor.close()
database.close()
