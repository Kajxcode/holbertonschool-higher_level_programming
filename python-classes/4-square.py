#!/usr/bin/python3
"""this module defines a class"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """intialise a new square

        args:
        size : size of square
        """
        self.size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        """sets the size of square
        args: value int 
        raises: type error, value error
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """defines area of square"""
        return self.__size ** 2
