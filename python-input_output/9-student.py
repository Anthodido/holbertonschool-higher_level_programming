#!/usr/bin/python3
"""Module: classe Student et conversion en dictionnaire."""


class Student:
    """Représente un étudiant."""
    def __init__(self, first_name, last_name, age):
        """Initialise un Student avec nom, prénom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourne un dict représentant l'instance."""
        return self.__dict__
