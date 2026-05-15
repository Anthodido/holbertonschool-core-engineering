#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    """Defines an abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method that defines the area behavior."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method that defines the perimeter behavior."""
        pass


class Rectangle(Shape):

    """Represents a rectangle that inherits from the Shape class."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        """Implements the area method for a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Abstract method that defines the perimeter behavior."""
        return 2 * (self.__width + self.__height)


class Circle(Shape):

    """Represents a circle that inherits from the Shape class."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        """Implements the area method for a circle."""
        return pi * (self.__radius ** 2)

    def perimeter(self):
        """Abstract method that defines the perimeter behavior."""
        return 2 * pi * self.__radius


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
