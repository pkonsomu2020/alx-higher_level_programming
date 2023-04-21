#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)

    # create cursor object
    cursor = db.cursor()

    # prepare SQL query with placeholders
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    # execute query with sanitized input
    cursor.execute(query, ("hbtn_0e_0_usa",))

    # fetch all results
    states = cursor.fetchall()

    # print results
    for state in states:
        print(state)

    # close database connection
    db.close()
