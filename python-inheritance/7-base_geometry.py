#!/usr/bin/python3
"""this module defines a class"""


class BaseGeometry:
    """class for base geometry"""

    def area(self):
        """method for area"""
        raise Exception("area () is not implemented")
    
    def integer_validator(self, name, value):
        """validates integer is positive
        
        Args:
        name
        value
        
        Raises:
        typeerror
        valueerror
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
