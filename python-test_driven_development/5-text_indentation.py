#!/usr/bin/python3
"""Module: text_indentation"""


def text_indentation(text):
    """Print a text with 2 new lines after each '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    skip_space = True

    for ch in text:
        if skip_space and ch == " ":
            continue

        buffer += ch
        skip_space = False

        if ch in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
            skip_space = True

    if buffer.strip() != "":
        print(buffer.strip(), end="")
