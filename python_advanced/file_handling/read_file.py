#!/usr/bin/env python3

"""Defines a function to read a text file and print its contents."""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
