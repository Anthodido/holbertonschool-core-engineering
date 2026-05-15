#!/usr/bin/env python3

"""Defines a Square class that inherits from BaseGeometry."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):

    """A class that defines a square by: (based on 0-square.py)"""

    def __init__(self, size):

        """Initialize the data."""

        super().__init__(size, size)
        self.__size = size

    def __str__(self):

        """Returns a string representation of the square."""

        return "[Square] {}/{}".format(self.__size, self.__size)
