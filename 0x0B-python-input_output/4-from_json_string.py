#!/usr/bin/python3
"""import json"""
import json

"""
Module returns the JSON representation of an object
"""


def from_json_string(my_str):
    """ Function that returns the JSON representation

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    return json.loads(my_str)
