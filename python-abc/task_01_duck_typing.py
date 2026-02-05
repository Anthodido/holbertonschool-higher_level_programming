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
        self.radius = abs(radius)

    def area(self):
        """Calcule et retourne l'aire de la forme."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Calcule et retourne le périmètre du cercle."""
        return 2 * pi * self.radius

    class Rectangle(Shape):
    """Classe représentant un rectangle défini par une largeur et une hauteur."""

    def __init__(self, width, height):
        """Initialise un rectangle.

        Args:
            width (float|int): largeur du rectangle.
            height (float|int): hauteur du rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)
