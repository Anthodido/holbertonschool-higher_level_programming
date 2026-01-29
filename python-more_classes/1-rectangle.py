#!/usr/bin/python3
"""Ce module définit une classe Rectangle."""


class Rectangle:
    """Initialise une nouvelle instance de Rectangle.
    size: taille du rectangle."""
    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une
        largeur et une hauteur optionnelles.
        Args:
        width (int): largeur du rectangle.
        height (int): hauteur du rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retourne la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
