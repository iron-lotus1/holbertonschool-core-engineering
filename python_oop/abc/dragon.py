#!/usr/bin/env python3

"""
Module defining SwimMixin, FlyMixin, and the Dragon class.
"""


class SwimMixin:
    """
    Mixin class that provides swimming capabilities.
    """

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capabilities.
    """

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a Dragon that can swim, fly, and roar.
    """

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
