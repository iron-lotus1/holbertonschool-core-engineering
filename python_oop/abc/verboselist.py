#!/usr/bin/env python3

"""
Module defining the VerboseList class extending Python's built-in list.
"""


class VerboseList(list):
    """
    A list subclass that prints a notification message whenever items
    are added (append, extend) or removed (remove, pop).
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and print a message.
        """
        items_list = list(iterable)
        count = len(items_list)
        super().extend(items_list)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a message.
        Raises ValueError if the item is not present.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index (default last) and print a message.
        Raises IndexError if list is empty or index is out of range.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
