#!/usr/bin/python3

"""
This is a module-level It provides singly linked list classes.
"""


class Node:
    """
    Node class represents a single element in a singly linked list.

    Attributes:
    - data: The data stored in the node (an integer).
    - next_node: A reference to the next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object next_node.

        Args:
        - data: The data to be stored in the node.
        - next_node: The next node in the linked list (default is None).

        Raises:
        - TypeError: If data is not an integer or not None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for the data attribute.

        Returns:
        - The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for the data attribute.

        Args:
        - value: The data to be set in the node.

        Raises:
        - TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("datamust be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter for the next_node attribute.

        Returns:
        - The next node in the linked list (a Node object).
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for the next_node attribute.

        Args:
        - value: The next node in the linked list (a Node object).

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.

    Methods:
    - sorted_insert(value): Inserts a new node with.
    - __str__(): Returns a string representation of the linked list.

    Attributes:
    - __head: A reference to the head (first node) of the linked list.
    """

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - A string containing the data of each node in the linked list.
        """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value into the linked list.

        Args:
        - value: The data to be stored in the new node.
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
