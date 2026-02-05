#!/usr/bin/python3


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Classe abstraite shape."""

    @abstractmethod
    def area(self):
        """Calcule et retourne l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calcule et retourne le périmètre de la forme."""
        pass


class Circle(Shape):

    def __init__(self, radius):
        """Classe représentant un cercle défini par un rayon."""
        self.radius = radius

    def area(self):
        """Calcule et retourne l'aire de la forme."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Calcule et retourne le périmètre du cercle."""
        return 2 * pi * self.radius
