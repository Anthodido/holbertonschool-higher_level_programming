#!/usr/bin/python3
"""Module: serialisation JSON simple d'un dictionnaire."""


import json


def serialize_and_save_to_file(data, filename):
    """Ecrit le dict data en JSON dans le fichier filename."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Lit filename (JSON) et retourne le dictionnaire Python."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
