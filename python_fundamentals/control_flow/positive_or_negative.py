#!/usr/bin/env python3

number = __import__('random').randint(-10, 10)

for number in range(-10, 10):
    if number > 0:
        print(number, "is positive")

    elif number == 0:
        print(number, "is zero")

    else:
        print(number, "is negative")
