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
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON  cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    states = cursor.fetchall()

    print(", ".join([state[1] for state in states]))
