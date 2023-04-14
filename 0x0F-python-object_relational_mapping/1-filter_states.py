#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # connect to database
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # create cursor object
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    # fetch all results
    results = cursor.fetchall()

    # print results
    for row in results:
        print(row)

    # close database connection
    db.close()
