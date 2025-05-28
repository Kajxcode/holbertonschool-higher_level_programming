#!/usr/bin/python3
"""this module defines a funciton the checks inheritance"""


def inherits_from(obj, a_class):
    """this method returns inheritance"""
    return isinstance(obj, a_class) and type(obj) is not a_class
