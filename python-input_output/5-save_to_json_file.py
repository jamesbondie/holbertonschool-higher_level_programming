#!/usr/bin/python3
"""IS DOCUMENTED"""
import json


def save_to_json_file(my_obj, filename):
    """IS DOCUMENTED"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
