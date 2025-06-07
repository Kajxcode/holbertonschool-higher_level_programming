#!/usr/bin/python3
"""this module reads a text file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
