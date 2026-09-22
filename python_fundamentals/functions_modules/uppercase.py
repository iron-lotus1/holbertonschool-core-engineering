#!/usr/bin/env python3

def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            char = (ord(char) - 32)
            print("{}".format(char), end="")
            print("")
