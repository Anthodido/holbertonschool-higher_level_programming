#!/usr/bin/python3
"""Module: conversion d'un fichier CSV en JSON."""


import csv
import json


def convert_csv_to_json(CSV_filename):
    """Convertit CSV_filename en JSON et écrit dans data.json."""
    try:
        with open(CSV_filename, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        with open("data.json", "w", encoding="utf-8") as out:
            json.dump(rows, out, indent=4)

        return True
    
    except FileNotFoundError:
        return False
