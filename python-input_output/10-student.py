#!/usr/bin/python3
"""Module: classe Student et conversion en dictionnaire."""


class Student:
    """Représente un étudiant."""
    def __init__(self, first_name, last_name, age):
        """Initialise un Student avec nom, prénom et âge."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retourne un dict représentant l'instance."""
        if type(attrs) is not list:
            return self.__dict__
        if not all(type(x) is str for x in attrs):
            return self.__dict__
        result = {}
        for name in attrs:
            if name in self.__dict__:
                result[name] = self.__dict__[name]
        return result
