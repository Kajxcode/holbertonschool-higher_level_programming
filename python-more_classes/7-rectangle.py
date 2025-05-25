#!/usr/bin/python3
"""Defines a Rectangle class with instance counting and customizable print symbol."""


class Rectangle:
    """Rectangle with width, height, instance count, and customizable print symbol."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle and increment the instance counter."""
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
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle, or 0 if width or height is 0."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using print_symbol."""
        if self.__width is 0 or self.__height is 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string to recreate the Rectangle via eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message and decrement instance count on deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
