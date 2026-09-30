#!/usr/bin/env python3

"""
Module defining an abstract Shape class, its Circle and Rectangle subclasses,
and a polymorphic shape_info helper function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle: π * r^2
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle: 2 * π * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the rectangle: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of any object implementing
    the area() and perimeter() methods via duck typing.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
