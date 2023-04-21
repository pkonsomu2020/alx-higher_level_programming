#!/usr/bin/python3
import MySQLdb

if __name__ == "__main__":
    # connect to database
    db = MySQLdb.connect(user="root", passwd="ponsomu756@", db="hbtn_0e_0_usa")

    # create cursor object
    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%';")

    # fetch all results
    states = cursor.fetchall()

    # print results
    for state in states:
        print(state)

# close database connection
cursor.close()
db.close();
