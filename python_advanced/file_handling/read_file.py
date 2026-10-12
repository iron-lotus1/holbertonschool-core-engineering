#!/usr/bin/env python3
"""Module that reads a UTF-8 text file and prints its contents."""

def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as read_data:
        print(read_data.read())
