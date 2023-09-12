#!/usr/bin/python3
"""import json"""
import json

"""
Module returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """ Function that returns the JSON representation

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
