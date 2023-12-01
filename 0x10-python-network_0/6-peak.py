#!/usr/bin/python3
"""Find a peak in a list"""


def find_peak(list_of_integers):
    """Method peak"""

    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    middle = int(length / 2)
    li = list_of_integers

    if middle - 1 < 0 and middle + 1 >= length:
        return li[middle]
    elif middle - 1 < 0:
        return li[middle] if li[middle] > li[middle + 1] else li[middle + 1]
    elif middle + 1 >= length:
        return li[middle] if li[middle] > li[middle - 1] else li[middle - 1]

    if li[middle - 1] < li[middle] > li[middle + 1]:
        return li[middle]

    if li[middle + 1] > li[middle - 1]:
        return find_peak(li[middle:])
    return find_peak(li[:middle])
