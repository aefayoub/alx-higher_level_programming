#!/usr/bin/python3

"""
Module based on Module 5
"""


class BaseGeometry:
    """Class contains area function"""

    def area(self):
        """
        raise exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that recieves the value property

        Árgs:
            name: name of the object
            value: value of the property

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

