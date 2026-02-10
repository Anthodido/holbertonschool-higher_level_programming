#!/usr/bin/python3
"""Module: décrit un objet en dict sérialisable JSON."""


def class_to_json(obj):
    """Retourne le dictionnaire des attributs d'instance."""
    return obj.__dict__
