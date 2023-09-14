#!/usr/bin/python3

"""
Module MyInt
"""


class MyInt(int):
    """Class Myint """

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
