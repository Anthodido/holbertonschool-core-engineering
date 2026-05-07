#!/usr/bin/env python3

"""Create a script that assigns a random integer to a variable"""

number = __import__('random').randint(-10, 10)

if number < 0:
    print(f"{number} is negative")

elif number == 0:
    print(f"{number} is zero")

else:
    print(f"{number} is positive")
