#!/usr/bin/python3

"""
Module that contains a function that reads from a file
"""


def append_write(filename="", text=""):
    """function read file nbr line"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
