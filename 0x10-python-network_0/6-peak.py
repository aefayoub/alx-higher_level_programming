#!/usr/bin/python3
"""Find a peak in a list"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    middle = int(length / 2)
    mylist = list_of_integers

    if middle - 1 < 0 and middle + 1 >= length:
        return mylist[middle]
    elif middle - 1 < 0:
        return mylist[middle] if mylist[middle] > mylist[middle + 1] else mylist[middle + 1]
    elif middle + 1 >= length:
        return mylist[middle] if mylist[middle] > mylist[middle - 1] else mylist[middle - 1]

    if mylist[middle - 1] < mylist[middle] > mylist[middle + 1]:
        return mylist[middle]

    if mylist[middle + 1] > mylist[middle - 1]:
        return find_peak(mylist[middle:])
    return find_peak(mylist[:middle])
