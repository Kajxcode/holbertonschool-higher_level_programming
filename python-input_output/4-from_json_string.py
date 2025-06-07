#!/usr/bin/python3
"""Module that provides a function to convert a JSON."""


import json


def from_json_string(my_str):
    """Returns a Python object represented by a JSON"""
    return json.loads(my_str)
