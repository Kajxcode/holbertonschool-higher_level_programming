#!/usr/bin/python3
"""returns a dictionary description of an object for JSON"""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON"""
    return obj.__dict__
