#!/usr/bin/python3

"""
Module append after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Class append after
    args:
        filename
        search_string
        new_string=
    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        """append content file"""

        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        """write content file"""
        f.write("".join(res_line))
