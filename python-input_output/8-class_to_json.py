#!/usr/bin/python3
"""Class to JSON."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    return obj.__dict__
