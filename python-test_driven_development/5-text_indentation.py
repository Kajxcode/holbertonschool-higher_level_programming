#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    output = ""
    while i < length:
        char = text[i]
        output += char
        if char in ['.', '?', ':']:
            output = output.rstrip() + char + "\n\n"
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    for line in output.splitlines():
        print(line.strip())
