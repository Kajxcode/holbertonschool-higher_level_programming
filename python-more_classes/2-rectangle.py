#!/usr/bin/python3
"""this module defines a class"""


class Rectangle:
    """defines a class called rectangle"""
    pass
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
         """retrieve width"""
         return self.__width

    @width.setter
    def width(self, value):
         """sets width"""
         if not isinstance(value, int):
            raise TypeError("width must be an integer")
         if value < 0:
            raise ValueError("width must be >= 0")
         self.__width = value
    
    @property
    def height(self):
        """retireves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
                raise TypeError("height must be an integer")
        if value < 0:
                raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
         return self.__height * self.__width
    
    def perimeter(self):
         if self.__width or self.__height is 0:
              return 0
         return 2 * (self.__height + self.__width)
