#!/usr/bin/python3
"""Module: ajout de texte en fin de fichier UTF-8."""


def append_write(filename="", text=""):
    """Ajoute text à filename et retourne le nb de caractères."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
