#!/usr/bin/python3
"""Module qui définit une classe vide BaseGeometry."""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Lève une exception car l'aire n'est pas implémentée."""
        raise Exception("area() is not implemented")
