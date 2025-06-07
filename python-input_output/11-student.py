#!/usr/bin/python3
"""this module defines a class called student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(self, attrs=None):
        """Returns the dictionary description of an object for JSON serialization"""
        if (type(attrs) is list and all(type(attr) is str for attr in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
    
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)