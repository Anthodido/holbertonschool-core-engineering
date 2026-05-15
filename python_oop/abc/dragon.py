#!/usr/bin/env python3

"""Defines a Dragon class that inherits from both SwimMixin and FlyMixin."""


class SwimMixin:
    """A mixin class that provides swimming behavior."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class that represents a dragon, which can both swim and fly."""
    def roar(self):
        print("The dragon roars!")
