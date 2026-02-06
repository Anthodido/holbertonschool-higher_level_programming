#!/usr/bin/python3
"""Module that defines a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Ret T obj est une instance de a_class ou d'une sous-classe."""
    return isinstance(obj, a_class)
