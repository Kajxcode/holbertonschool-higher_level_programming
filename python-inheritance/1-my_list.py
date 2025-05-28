#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that adds a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
