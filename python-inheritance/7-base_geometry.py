#!/usr/bin/python3
"""Module qui définit une classe vide BaseGeometry."""


class BaseGeometry:
    def area(self):
        """Lève une exception car l'aire n'est pas implémentée."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valide que value est un entier strictement positif."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
