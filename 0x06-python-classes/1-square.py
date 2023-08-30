#!/usr/bin/python3

"""
iThis is a module-level docstring. It provides an overview of the class square.
"""


class Square:
    """
    The Square class represents a square shape.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size): Initializes a new Square instance.

    Note:
        Double underscores before a variable or method name.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
