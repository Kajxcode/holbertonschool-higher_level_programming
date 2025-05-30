#!/usr/bin/python3
"""This module defines a Square class that inherits from
 9-rectangle.Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """Returns string representation"""
        return f"[Square] {self.__size}/{self.__size}"
