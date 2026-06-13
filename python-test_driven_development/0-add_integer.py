#!/usr/bin/python3
"""This module provides a function that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
