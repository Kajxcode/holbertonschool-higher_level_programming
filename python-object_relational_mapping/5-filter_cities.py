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
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_searched,)
    )
    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
