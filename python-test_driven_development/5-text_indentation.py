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
    segment = ""

    while i < length:
        char = text[i]
        if char in ['.', '?', ':']:
            segment = segment.rstrip()  # remove trailing spaces before punctuation
            print(segment + char)
            print()  # print single blank line
            i += 1
            # Skip all spaces after punctuation to avoid leading spaces in next line
            while i < length and text[i] == ' ':
                i += 1
            segment = ""  # reset segment for next line
        else:
            segment += char
            i += 1

    # Print remaining text if any (strip trailing spaces)
    if segment:
        print(segment.rstrip())
