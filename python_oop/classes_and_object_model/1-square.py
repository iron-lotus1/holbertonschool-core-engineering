#!/usr/bin/env python3

"""Module that defines a Square class."""


class Square:
    """Defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of a side of the square.
        """
        self.__size = size
