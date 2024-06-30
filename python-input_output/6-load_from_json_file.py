#!/usr/bin/python3
"""IS DOCUMENTED"""
import json


def load_from_json_file(filename):
    """IS DOCUMENTED"""
    with open(filename, 'r', encoding='utf-8') as f:
        x = f.read()
    return json.loads(x)
