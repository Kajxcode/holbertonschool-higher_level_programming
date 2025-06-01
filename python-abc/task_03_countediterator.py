#!/usr/bin/python3
"""this module defiines a class"""


class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        return self._count

