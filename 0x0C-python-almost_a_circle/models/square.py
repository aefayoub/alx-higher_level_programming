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

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute"""

        if args is not None and len(args) != 0:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, key, value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
