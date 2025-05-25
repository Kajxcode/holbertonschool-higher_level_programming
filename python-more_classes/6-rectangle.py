#!/usr/bin/python3
"""This module defines a Rectangle class with instance counting."""


class Rectangle:
    """Defines a Rectangle with width and height, and tracks instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter, or 0 if width or height is 0."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using '#'."""
        if self.__width is 0 or self.__height is 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string that recreates the instance with eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message and decrement instance counter when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
