#!/usr/bin/python3

""" 
This script conects to a database, create a cursor object
selct rows, print them and close the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    args = argv

    connect_db = MySQLdb.connect(
        host="localhost", user=args[1], passwd=args[2], db=args[3], port=3306
    )

    cur = connect_db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connect_db.close()
