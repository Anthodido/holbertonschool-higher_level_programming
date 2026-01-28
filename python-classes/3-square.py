#!/usr/bin/python3
"""Ce module définit une classe Square avec une taille et une méthode area."""


class Square:
    """classe square"""
    def __init__(self, size=0):
        """Initialise un carré avec une taille optionnelle.
        Args:
            size (int): taille du carré.
        Raises:
            TypeError: si size n'est pas un entier.
            ValueError: si size est inférieur à 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size
