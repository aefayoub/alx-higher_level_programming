#!/usr/bin/python3

"""
Module that adds new attribute
"""


def add_attribute(obj, name, value):
    """
    Function that adds a new attribute.
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
