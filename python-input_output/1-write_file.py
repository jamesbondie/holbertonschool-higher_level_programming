#!/usr/bin/python3
"""IS DOCUMENTED"""


def write_file(filename="", text=""):
    """IS DOCUMENTED"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
