#!/usr/bin/python3
"""Module: conversion d'objets Python en chaîne JSON."""


import json


def to_json_string(my_obj):
    """Retourne la représentation JSON (str) d'un objet."""
    return json.dumps(my_obj)
