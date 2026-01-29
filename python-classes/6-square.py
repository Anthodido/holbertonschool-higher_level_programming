#!/usr/bin/python3
"""Ce module définit une classe Square avec une taille et une méthode area."""


class Square:
    """classe square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille optionnelle.
        Args:
            size (int): taille du carré.
        Raises:
            TypeError: si size n'est pas un entier.
            ValueError: si size est inférieur à 0."""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Retourne la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Modifie la taille du carré."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not isinstance(value[0], int) or not isinstance(value[1], int) or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Retourne la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifie la taille du carré."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size * self.__size

    def my_print(self):
        """Imprime le carré avec le caractère # en tenant compte de la position."""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
