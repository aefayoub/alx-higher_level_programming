#!/usr/bin/python3

"""
Module student to json.
"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function returns json"""

        obj = self.__dict__.copy()
        return obj
