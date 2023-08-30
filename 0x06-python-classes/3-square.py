#!/usr/bin/python3

"""
This is a module-level docstring. It provides an overview of the class square.
"""


class Square:
    """
    The Square class represents a square shape.

    Attributes:
        __size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0): Initializes a new Square instance.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is a negative integer.

    Note:
        Double underscores before a variable or method name, like __size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square's sides.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is a negative integer.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size ** 2)
