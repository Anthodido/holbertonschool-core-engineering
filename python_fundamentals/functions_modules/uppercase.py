#!/usr/bin/env python3

def uppercase(str):
    for index in str:
        if ord(index) >= ord('a') and ord(index) <= ord('z'):
            index = chr(ord(index) - (ord('a') - ord('A')))
        print(index, end="")
    print()
