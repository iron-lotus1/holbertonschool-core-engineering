#!/usr/bin/env python3

"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A foundational class for geometric shapes."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter (used in error messages).
            value (int): The parameter value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
