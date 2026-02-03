#!/usr/bin/python3
"""Module qui définit une classe vide BaseGeometry."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
