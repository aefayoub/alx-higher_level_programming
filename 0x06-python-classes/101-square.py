#!/usr/bin/python3

"""
This is a module-level It provides singly linked list classes.
"""


class Square:
    """
    A class that represents a square defined by its size and position.

    Attributes:
        size (int): The length of each side of the square.
        position (tuple): A tuple representing the position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)):
            Initializes a new Square instance with a given size and position.

        __str__(self):
            Returns a string representation of the square.
            Takes the square's position into account for rendering.

        size (property):
            Gets the size of the square.

        size (setter):
            Sets the size of the square.

        position (property):
            Gets the position of the square.

        position (setter):
            Sets the position of the square.

        area(self):
            Calculates and returns the area of the square.

        my_print(self):
            Prints the square to the console.
            Adjusts the position of the square as specified.

    Example Usage:
        # Create a square with size 3 and position (1, 2)
        my_square = Square(3, (1, 2))

        # Display the square
        print(my_square)
        # Output:
        #
        #
        #  ###
    """

    def __str__(self):
        """
        Returns a string representation of the square.

        The string represents the square as a pattern of '#' charactere.

        Returns:
            str: A string representation of the square.
        """

        rtn = ""

        if self.size == 0:
            return rtn

        for i in range(self.position[1]):
            rtn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rtn += " "
            for j in range(self.size):
                rtn += "#"
            if i is not (self.size - 1):
                rtn += "\n"

        return rtn

    def __init__(self, size=0, position=(0, 0)):
        """
        Method to initialize the square object
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
