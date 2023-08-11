#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    nargs = len(argv)
    sumargs = 0
    for i, arg in enumerate(argv, start=1):
        sumargs += int(arg)
    print(sumargs)
