#!/usr/bin/python3
"""import json"""
import json

"""
Module returns the JSON representation of an object
"""


def save_to_json_file(my_obj, filename):
    """ Function that returns the JSON representation

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
