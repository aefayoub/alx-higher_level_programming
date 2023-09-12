#!/usr/bin/python3
"""Import BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle

"""
Module based on Module 5
"""


class Square(Rectangle):
    """Class contains __int__ function"""

    def __init__(self, size):
        """Initialisation"""

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method that returns the area of the instance"""
        return super().area()

    def __str__(self):
        """Special method that returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
