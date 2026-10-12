#!/usr/bin/env python3

"""function that writes a string to a text file"""

def write_file(filename="", text=""):
    """Write a string to a UTF-8 file and return the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as my_first_file:
        nb_characters = my_first_file.write(text)
        return nb_characters
