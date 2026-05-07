#!/usr/bin/env python3

for i in range(0, 99 + 1):
    if i != 99:
        print("{0:02d}".format(i), end=", ")
    else:
        print("{0:02d}".format(i))
