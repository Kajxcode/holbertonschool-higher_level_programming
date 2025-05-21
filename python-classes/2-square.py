#!/usr/bin/python3
"""this module defines a class"""


class Square:
    """defines a square"""
    pass
    def __init__(self, size):
        """intialise a new square

        args:
        size : size of square
        """
        self.__size = size

        if size is not int:
            raise TypeError("size must be an integer")
        if size >= 0:
            raise ValueError("size must be >= 0")
