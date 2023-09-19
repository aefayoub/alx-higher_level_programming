#!/usr/bin/python3
"""imports"""
import json

"""
Module that contains class Base
"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """List to json string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """function permet to save object in a file"""
        file_name = "{}.json".format(cls.__name__)
        dic_attr = []
        lists = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                dic_attr.append(list_objs[i].to_dictionary())
        lists = cls.to_json_string(dic_attr)

        with open(file_name, "w") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """ from json to string """
        if not json_string:
            return []
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Create an instance"""
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new
