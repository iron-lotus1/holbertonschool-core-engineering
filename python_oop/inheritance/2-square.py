#!/usr/bin/env python3
"""
Module that defines a Square class inheriting from Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a square using Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
