#!/usr/bin/python3
"""IS DOCUMENTED"""


def read_file(filename=""):
    """IS DOCUMENTED"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
