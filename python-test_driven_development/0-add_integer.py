#!/usr/bin/python3
"""Add integer module.
Provides add_integer function.
Validates types.
Casts floats to ints.
Returns integer sum.
"""


def add_integer(a, b=98):
    """Add two numbers as integers.
Floats are cast to ints.
Raises TypeError on bad types.
"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
