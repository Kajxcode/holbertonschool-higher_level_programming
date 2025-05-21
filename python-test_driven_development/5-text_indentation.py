#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with a new line after each '.', '?', and ':' character.
    Removes leading spaces at the beginning of each printed line.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    buffer = ""

    while i < length:
        char = text[i]
        buffer += char

        if char in ['.', '?', ':']:
            print(buffer.strip())
            buffer = ""
            i += 1
            # skip spaces
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    if buffer.strip():
        print(buffer.strip())
