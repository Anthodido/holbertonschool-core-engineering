#!/usr/bin/env python3

"""Defines a FlyingFish class that inherits from BaseGeometry."""


class Bird:

    """Represents a bird."""

    def fly(self):
        """Defines the flying behavior of the bird."""
        print("The bird is flying")

    def habitat(self):
        """Defines the habitat of the bird."""
        print("The bird lives in the sky")


class Fish:

    """Represents a fish."""

    def habitat(self):
        """Defines the habitat of the fish."""
        print("The fish lives in water")

    def swim(self):
        """Defines the swimming behavior of the fish."""
        print("The fish is swimming")


class FlyingFish(Bird, Fish):

    """Represents a flying fish that inherits
    from both Bird and Fish classes."""

    def fly(self):
        """Defines the flying behavior of the flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Defines the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")

    def swim(self):
        """Defines the swimming behavior of the flying fish."""
        print("The flying fish is swimming!")
