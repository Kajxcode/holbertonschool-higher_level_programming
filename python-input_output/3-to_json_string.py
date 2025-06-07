#!/usr/bin/python3
"""Module that provides a function to convert a Python object to a JSON"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    return json.dumps(my_obj)
