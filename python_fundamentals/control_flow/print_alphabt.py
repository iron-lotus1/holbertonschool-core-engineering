#!/usr/bin/env python3

text = "abcdefghijklmnopqrstuvwxyz"
exclude = "eq"

alpha = ''.join([char for char in text if char not in exclude])
print(alpha)
