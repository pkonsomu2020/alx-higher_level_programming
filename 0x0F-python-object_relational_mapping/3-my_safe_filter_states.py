#!/usr/bin/python3
import MySQLdb

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user="root", passwd="ponsomu756@", db="hbtn_0e_0_usa")

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
