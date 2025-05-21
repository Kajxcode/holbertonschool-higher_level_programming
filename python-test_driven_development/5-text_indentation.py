#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints text with a newline after each '.', '?' or ':' character.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ['.', '?', ':']:
            print(buffer.strip())
            buffer = ""
    if buffer.strip():  # Print remaining text if any
        print(buffer.strip())
