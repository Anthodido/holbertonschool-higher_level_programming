#!/usr/bin/python3


class VerboseList(list):
    """Liste verbeuse héritant de list et notifiant les modifications."""

    def append(self, item):
        """Ajoute un élément à la liste et affiche un message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Étend la liste avec plusieurs éléments."""
        items = list(items)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Supprime un élément de la liste."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Retire et retourne un élément de la liste."""
        value = super().pop(index)
        print(f"Popped [{value}] from the list.")
        return value
