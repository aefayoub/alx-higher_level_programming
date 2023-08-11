#!/usr/bin/python3

import sys

def arguments():
    argv = sys.argv[1:]
    nargs = len(argv)

    if nargs == 0:
        print("0 arguments.")
    else:
        print(f"{nargs} {'argument' if nargs == 1 else 'arguments'}:")

        for i, arg in enumerate(argv, start = 1):
            print(f"{i}: {arg}")

arguments()
