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
    cur.execute('SELECT cities.name FROM cities WHERE state.id = (SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY cities.id;', (argv[4]))
    
    rows = cur.fetchall()
    
    print(", ".join([row[1] for row in rows]))
    
    cur.close()
    connect_db.close()
