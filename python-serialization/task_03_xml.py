#!/usr/bin/python3
"""Module: conversion d'un fichier CSV en JSON."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialise un dictionnaire en XML et l'écrit dans filename."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")

def deserialize_from_xml(filename):
    """Désérialise un fichier XML et retourne un dictionnaire Python."""
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = "" if child.text is None else child.text
    return data
