#!/usr/bin/env python3

text = ""
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != "e" and letter != "q":
        text += letter
print(text)
