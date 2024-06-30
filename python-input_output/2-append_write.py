#!/usr/bin/python3
"""IS DOCUMENTED"""


def append_write(filename="", text=""):
    """IS DOCUMENTED"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
