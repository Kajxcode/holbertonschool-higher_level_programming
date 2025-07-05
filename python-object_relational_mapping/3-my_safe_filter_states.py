#!/usr/bin/python3
"""
script that takes an argument and displays all values that match
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name

    )
    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = %s "
        "ORDER BY id ASC"
    )
    cur.execute(query, (state_searched,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
