#!/usr/bin/env python3

"""Defines a Square class."""


class Square:

        """Represents a square."""

    def __init__(self, size):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
