#!/usr/bin/python3
"""IMPORTING CSV, JSON"""
import csv
import json


def convert_csv_to_json(csvname):
    """CONVERTING CSV TO JSON"""
    try:
        with open(csvname, encoding='utf-9', newline='') as csvfile:
            x = csv.DictReader(csvfile)
            data = [row for row in x]
    except Exception:
        return False

    try:
        with open("data.json", 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
    except Exception:
        return False
    return True
