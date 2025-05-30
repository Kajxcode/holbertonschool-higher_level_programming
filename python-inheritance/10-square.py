#!/usr/bin/python3
"""This module defines a Square class that inherits from
 9-rectangle.Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size):
        self.__size = size

    def integer_validator(self, name, value):
        """validates integer is positive

        Args:
        name
        value

        Raises:
        typeerror
        valueerror
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Returns the area of the rectangle"""
        return self.__size * self.__size
