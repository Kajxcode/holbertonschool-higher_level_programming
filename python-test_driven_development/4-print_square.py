#!/usr/bin/python3
"""
This module defines a function
"""
def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float):
        raise
