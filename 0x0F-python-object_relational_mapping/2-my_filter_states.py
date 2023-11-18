#!/usr/bin/python3
"""
script that lists all states from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * \
            FROM states \
            WHERE CONVERT(`name` USING Latin1) \
            COLLATE Latin1_General_CS \
            like '{}';".format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)
