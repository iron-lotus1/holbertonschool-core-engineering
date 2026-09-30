#!/usr/bin/env python3

"""
Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Print swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Print flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish inheriting from both Fish and Bird.
    """

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")

