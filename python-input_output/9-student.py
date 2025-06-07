#!/usr/bin/python3
"""this module defines a class called student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description of an object for JSON"""
        return self.__dict__
