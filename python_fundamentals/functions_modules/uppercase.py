#!/usr/bin/env python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(char) - 32)
            print("{}".format(char), end="")
            print("")
