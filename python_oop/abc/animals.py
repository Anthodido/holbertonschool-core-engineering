#!/usr/bin/env python3

"""Defines an abstract base class for animals."""

from abc import ABC, abstractmethod


class Animal(ABC):

    """Defines an abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that defines the sound behavior."""
        pass


class Dog(Animal):

    """Represents a dog that inherits from the Animal class."""

    def sound(self):
        """Implements the sound method for a dog."""
        return "Bark"


class Cat(Animal):

    """Represents a cat that inherits from the Animal class."""

    def sound(self):
        """Implements the sound method for a cat."""
        return "Meow"
