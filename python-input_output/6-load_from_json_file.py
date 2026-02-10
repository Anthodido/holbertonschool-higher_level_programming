#!/usr/bin/python3
"""Module: chargement d'un objet Python depuis un fichier JSON."""


import json


def load_from_json_file(filename):
    """Charge et retourne un objet Python depuis un fichier JSON."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
