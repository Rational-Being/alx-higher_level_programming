#!/usr/bin/python3

""" 
This script conects to a database, create a cursor object
selct rows, print them and close the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
   
    connect_db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    
    cur = connect_db.cursor()
    cur.execute('SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id;')
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    connect_db.close()
