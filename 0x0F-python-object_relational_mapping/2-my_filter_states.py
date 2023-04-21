#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)

    # create cursor object
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states WHERE name= %s \
            ORDER BY states.id ASC", ("hbtn_0e_0_usa",))

    # fetch all results
    states = cursor.fetchall()

    # print results
    for state in states:
        print(state)

    # close database connection
    cursor.close()
    db.close()
