#!/usr/bin/python3
"""import json"""
import json

"""
Module returns the JSON representation of an object
"""


def load_from_json_file(filename):
    """ Function that returns the JSON representation

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
