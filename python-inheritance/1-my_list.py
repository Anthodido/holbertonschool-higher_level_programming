#!/usr/bin/python3
class MyList(list):
    """sous-classe de list qui peut afficher ses éléments triés."""

    def print_sorted(self):
        """Affiche la liste triée par ordre croissant"""
        print(sorted(self))
