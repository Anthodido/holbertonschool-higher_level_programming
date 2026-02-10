#!/usr/bin/python3
"""Module: sauvegarde d'un objet Python en JSON dans un fichier."""


import json


def save_to_json_file(my_obj, filename):
    """Écrit un objet Python dans un fichier au format JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
