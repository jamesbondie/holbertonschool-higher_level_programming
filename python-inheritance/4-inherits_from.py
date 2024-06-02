#!/usr/bin/python3
"""IS DOCUMENTED"""


def inherits_from(obj, a_class):
    """IS DOCUMENTED"""
    return type(obj) is not a_class and isinstance(obj, a_class)
