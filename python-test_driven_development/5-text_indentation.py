#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")

        if char in ".?:":
            print("\n")
            # Skip spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
