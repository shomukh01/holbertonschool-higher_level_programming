#!/usr/bin/python3
"""Module that contains the class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    return obj.__dict__
