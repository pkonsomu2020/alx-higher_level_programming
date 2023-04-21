#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         host="localhost", port=3306)

    # create cursor object
    cursor = db.cursor()

    # prepare SQL query
    query = ("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id \
            = states.id ORDER BY cities.id ASC")

    # execute query
    cursor.execute(query)

    # fetch all results
    states = cursor.fetchall()

    # print results
    for state in states:
        print(state)

    # close database connection
    db.close()
