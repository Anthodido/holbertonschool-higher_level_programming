#!/usr/bin/python3
"""Ce module définit une classe Square avec une taille validée."""


class Square:
    """Initialise un carré avec une taille optionnelle.
    size (int): taille du carré.
    TypeError: si size n'est pas un entier.
    ValueError: si size est inférieur à 0."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
