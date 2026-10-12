#!/usr/bin/env python3
"""Functionm that appends a string at the end of text file"""


def append_write(filename="", text=""):
    """Returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as file_append:
        nb_characters_added = file_append.write(text)
        return nb_characters_added
