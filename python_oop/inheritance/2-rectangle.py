#!/usr/bin/env python3

"""
Module that defines a Rectangle class inheriting from BaseGeometry.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represent a rectangle using BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
