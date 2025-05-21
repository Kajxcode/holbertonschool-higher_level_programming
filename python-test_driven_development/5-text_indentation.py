#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    segment = ""

    while i < length:
        char = text[i]
        segment += char
        if char in ['.', '?', ':']:
            print(segment.strip())
            print()
            segment = ""
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    if segment:
        print(segment.strip())
