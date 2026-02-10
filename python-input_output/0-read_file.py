#!/usr/bin/python3
"""Module qui définit une fonction pour lire un fichier texte UTF-8."""


def read_file(filename=""):
    """Lit un fichier texte UTF-8 et affiche son contenu."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
