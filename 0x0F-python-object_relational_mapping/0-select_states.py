#!/usr/bin/python3
"""
script that lists all states from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)
    cursor =db.cursor()
    cursor.execute("SELECT * FROM states;")
    states = cursor.fetchall()

    for state in states:
        print(state)
