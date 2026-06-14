#!/usr/bin/python3
"""This module provides a function that adds two integers.

The function accepts integers and floats only.
Float values are cast to integers before addition.
Invalid argument types raise TypeError with specific messages.
"""


def add_integer(a, b=98):
    """Add two integers after validating and casting float values.

    Args:
        a: First integer or float.
        b: Second integer or float, defaults to 98.

    Returns:
        The integer sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
