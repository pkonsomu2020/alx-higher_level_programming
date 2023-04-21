#!/usr/bin/python3
import MySQLdb

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user="root", passwd="ponsomu756@", db="hbtn_0e_0_usa")

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
