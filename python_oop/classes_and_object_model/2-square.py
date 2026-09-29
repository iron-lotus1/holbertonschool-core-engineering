#!/usr/bin/env python3

Here is the updated Square class with type and value validation for size, along with a default value of 0 to handle optional instantiation.

Python
#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Defines a square by its size with type and value validation."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of a side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
