#!/usr/bin/env python3

def uppercase(str):
    for index in str:
        if ord(index) >= ord('a') ord(index) <= ord('z'):
            index = chr(ord(index) - 32)
        print("{}".format(index), end="")
    print()
