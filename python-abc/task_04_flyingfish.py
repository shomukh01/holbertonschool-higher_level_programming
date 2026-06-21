#!/usr/bin/python3
"""
Module that defines Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Represents a fish.
    """

    def swim(self):
        """Print swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat message."""
        print("The fish lives in water")


class Bird:
    """
    Represents a bird.
    """

    def fly(self):
        """Print flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish.
    """

    def fly(self):
        """Override fly."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat."""
        print("The flying fish lives both in water and the sky!")
