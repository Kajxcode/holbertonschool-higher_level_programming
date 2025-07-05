#!/usr/bin/python3
"""
lists all states from a database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    db.close()