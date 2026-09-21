#!/usr/bin/env python3

text = "abcdefghijklmnopqrstuvwxyz"
exclude = "e, q"

alpha = ''.join([char for char in text if char not in exclude])
print(alpha)
