#!/usr/bin/python3
"""importing json"""
import json


def serialize_and_save_to_file(data, filename):
    """serializing and saving"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    pass


def load_and_deserialize(filename):
    """loading and deserializing"""
    with open(filename, 'r') as file:
        return json.load(file)
    pass
