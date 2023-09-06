#!/usr/bin/python3

"""
This is a module that containts a clas that avoids
dynmaically created attributes
"""


class LockedClass:
    """
    A class with restricted attribute.

    Attributes:
        first_name (str): The first name.

    Note:
        This class uses __slots__ to limit attribute.
        Attempts to create or access other attributes.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """
        __init__ method
        """
        pass
