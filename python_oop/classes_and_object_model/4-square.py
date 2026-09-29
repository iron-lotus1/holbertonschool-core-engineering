#!/usr/bin/env python3

"""Module that defines a Square class."""


class Square:
    """Defines a square by its size with properties,
    validation, and area computation."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
