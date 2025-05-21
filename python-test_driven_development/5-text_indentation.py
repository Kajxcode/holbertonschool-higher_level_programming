#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with a new line after each '.', '?', or ':'.
    There are no extra blank lines, and no space at the start or end of each printed line.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    line = ""
    while i < length:
        char = text[i]
        line += char
        if char in ".?:":  # Time to print the line
            print(line.strip())
            line = ""
            i += 1
            # Skip spaces immediately after punctuation
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    if line.strip():
        print(line.strip())
