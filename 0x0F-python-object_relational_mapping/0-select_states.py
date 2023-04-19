#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user="root", passwd="ponsomu756@", db="hbtn_0e_0_usa")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
