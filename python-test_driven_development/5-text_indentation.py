#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """Prints text with two newlines after each '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    line = ''
    for char in text:
        line += char
        if char in delimiters:
            print(line.strip())
            line = ''
    if line.strip():
        print(line.strip())
