#!/usr/bin/python3

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user="root", passwd="ponsomu756@", db="hbtn_0e_0_usa")

    # create cursor object
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states")

    # fetch all results
    states = cursor.fetchall()

    # print results
    print(len(states))

    # close database connection
    cursor.close()
    db.close()
