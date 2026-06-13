#!/usr/bin/python3
"""Module that contains add_integer function."""


def add_integer(a, b=98):
    """Add two integers after casting floats to integers."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except ValueError:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except ValueError:
        raise TypeError("b must be an integer")

    return a + b
