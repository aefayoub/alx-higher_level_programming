#!/usr/bin/python3

"""
Module based on Module 5
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Class contains __int__ function"""

    def __init__(self, width, height):
        """Initialisation"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("heigt", height)
