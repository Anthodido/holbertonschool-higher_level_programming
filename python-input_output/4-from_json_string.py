#!/usr/bin/python3
"""Module: conversion d'une chaîne JSON en objet Python."""


import json


def from_json_string(my_str):
    """Retourne l'objet Python représenté par une chaîne JSON."""
    return json.loads(my_str)
