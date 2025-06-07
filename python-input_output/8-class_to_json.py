#!/usr/bin/python3
"""returns a dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization"""
    return obj.__dict__
