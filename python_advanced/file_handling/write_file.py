#!/usr/bin/env python3

"""Defines a function to write a string to a text file."""


def write_file(filename="", text=""):

    """string to a text file (UTF8) and returns the number of characters."""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
