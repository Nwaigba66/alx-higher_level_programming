#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__  == "__main__":
    username: str = sys.argv[1]
    passw0rd: str = sys.argv[2]
    db_name:  str = sys.argv [3]
    host: str = "hostname"
    port: INT = 3306
    statement: str = """SELECT * FROM states ORDER BY id
    

conn = MySQLdb.connect()
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
query_rows = cursor.fetchahh;
for ros in query_rows:
    
