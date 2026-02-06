#!/usr/bin/python3
"""Module that defines a function to check exact class matching."""


def is_same_class(obj, a_class):
    """Retourne True si obj est exactement une instance, sinon False."""
    return type(obj) is a_class
