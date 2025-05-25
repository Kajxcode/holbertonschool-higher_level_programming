#!/usr/bin/python3
"""this module defines a class"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """intialise a new square

        args:
        size : size of square
        position: square
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """print square with #"""
        if self.__size is 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
        
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
        

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    