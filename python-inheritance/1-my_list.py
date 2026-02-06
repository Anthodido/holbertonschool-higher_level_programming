#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """sous-classe de list qui peut afficher ses éléments triés."""

    def print_sorted(self):
        """Affiche la liste triée par ordre croissant"""
        print(sorted(list(self)))
