#!/usr/bin/python3
"""définit une classe abstraite Animal et ses sous-classes Dog et Cat."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite représentant un animal."""

    @abstractmethod
    def sound(self):
        """Retourne le son produit par l'animal."""
        pass


class Dog(Animal):

    """Classe représentant un chien."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Classe représentant un chat."""
    def sound(self):
        return "Meow"
