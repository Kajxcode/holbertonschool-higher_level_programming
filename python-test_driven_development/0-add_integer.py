#!/usr/bin/python3
"""
Module add_integer
Defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be int or float (otherwise raise TypeError).
    Any float inputs are truncated to int before addition.

    >>> add_integer(1, 2)
    3
    >>> add_integer(1.5, 2.5)
    3
    >>> add_integer(-1, 1)
    0
    >>> add_integer(1)
    99
    >>> add_integer("1", 2)
    Traceback (most recent call last):
       ...
    TypeError: a must be an integer
    >>> add_integer(1, "2")
    Traceback (most recent call last):
       ...
    TypeError: b must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
