#!/usr/bin/python3
"""Module: sérialisation/désérialisation d'un objet avec pickle."""


import pickle


class CustomObject:
    """Objet simple sérialisable via pickle."""

    def __init__(self, name, age, is_student):
        """Initialise l'objet avec name, age et is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs au format demandé."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Sérialise l'instance dans filename. Retourne None si erreur."""
        try:
            if not filename:
                return None
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge filename et renvoie un objet. None si fichier invalide."""
        try:
            with open(filename, "rb") as fi:
                return pickle.load(fi)
        except Exception:
            return None
