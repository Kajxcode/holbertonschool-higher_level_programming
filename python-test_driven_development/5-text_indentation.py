#!/usr/bin/python3
"""
This module defines a function
"""


def text_indentation(text):
    """
    Prints a text with a newline after each occurrence of '.', '?', and ':'.
    There should be no spaces at the beginning or end of each printed line.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    result = ""
    while i < length:
        char = text[i]
        result += char
        if char in ".?:":

            # Skip any following spaces
            i += 1
            while i < length and text[i] == " ":
                i += 1

            result += "\n"
            continue
        i += 1

    # Remove trailing whitespace-only lines and strip lines
    lines = [line.strip() for line in result.split("\n") if line.strip()]

    for line in lines:
        print(line)  # Always includes \n
