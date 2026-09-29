#!/usr/bin/env python3

"""Module that defines a Square class."""


class Square:
    """Defines a square by its size and position with properties and printing capabilities."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The side length of the square. Defaults to 0.
            position (tuple): Offset (x, y) coordinates for printing. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculate and return the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square in stdout using the '#' character and position offset."""
        print(self.__str__(), end="" if self.__size == 0 else "\n")

    def __str__(self):
        """Return the string representation of the square for printing."""
        if self.__size == 0:
            return ""

        res = []
        # Print vertical offset (newlines)
        res.append("\n" * self.__position[1])

        # Print horizontal offset (spaces) followed by '#' characters
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(res)
