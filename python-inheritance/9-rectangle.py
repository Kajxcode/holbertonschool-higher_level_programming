#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from
 7-base_geometry.BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits area() behavior and integer_validator()
 from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string version"""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    print(issubclass(Rectangle, BaseGeometry))
