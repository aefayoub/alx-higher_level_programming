#!/usr/bin/python3

"""
Module based on Module 5
"""


class Rectangle(BaseGeometry):
    """Class contains __int__ function"""

    """Import BaseGeometry class"""
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

    def __init__(self, width, height):
        """Initialisation"""

        self.__width = widthi
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
