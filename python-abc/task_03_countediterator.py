#!/usr/bin/python3
"""this module defiines a class"""


class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)  # Get the actual iterator
        self.count = 0                   # Count of items iterated

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)     # Get next item
        self.count += 1                 # Increment counter
        return item
