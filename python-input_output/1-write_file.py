#!/usr/bin/python3
"""Module: écriture d'un texte dans un fichier UTF-8."""


def write_file(filename="", text=""):
    """Écrit text dans filename et retourne le nb de caractères."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
