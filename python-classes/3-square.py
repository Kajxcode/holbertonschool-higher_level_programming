#!/usr/bin/python3
"""this module defines a class"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """intialise a new square

        args:
        size : size of square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        def area(self):
            """defines area of square"""
            return self.__size ** 2
