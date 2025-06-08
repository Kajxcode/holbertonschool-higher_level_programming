#!/usr/bin/python3
"""Defines a class customobject serialization w pickle"""

import pickle
import os


class CustomObject:
    """custom clas wsith name age and is_student"""
    def __init__(self, name, age, is_student)
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        try:
            with open(filename, 'wb')as f:
                pickle.dump(self, f)
        except(pickle.PickleError, OSError):
             return None
    
    @classmethod
    def deserealize(cls, filename):
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except(pickle.PickleError, OSError, EOFError):
            return None
