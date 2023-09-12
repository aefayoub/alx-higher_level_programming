#!/usr/bin/python3

"""
Module that contains a function that reads from a file
"""


def write_file(filename="", text=""):
    """function read file nbr line"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
