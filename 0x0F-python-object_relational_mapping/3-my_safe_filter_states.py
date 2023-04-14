#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to database
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    # create cursor object
    cursor = db.cursor()

    # prepare SQL query with placeholders
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    # execute query with sanitized input
    cursor.execute(query, (sys.argv[4],))

    # fetch all results
    results = cursor.fetchall()

    # print results
    for row in results:
        print(row)

    # close database connection
    db.close()
