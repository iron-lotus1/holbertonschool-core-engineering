#!/usr/bin/env python3

"""
Module defining an abstract Animal class and its Dog and Cat subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to return the animal's sound.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog, inheriting from Animal.
    """

    def sound(self):
        """
        Return the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a cat, inheriting from Animal.
    """

    def sound(self):
        """
        Return the sound made by a cat.
        """
        return "Meow"
