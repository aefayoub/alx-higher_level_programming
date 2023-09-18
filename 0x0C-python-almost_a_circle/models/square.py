#!/usr/bin/python3
"""import Module Rectangle"""
from models.rectangle import Rectangle

"""
Definition of Module Square.
"""


class Square(Rectangle):
    """Definition of class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method so that it returns [Square] informations"""

        str_id = " ({}) ".format(self.id)
        str_x_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}/{}".format(self.width, self.height)

        return "[Square]" + str_id + str_x_y + str_size
