#!/usr/bin/python3
"""Module is documented"""


def add_attribute(self, name1, name2):
    """Function is documented"""
    if hasattr(self, "__dict__"):
        setattr(self, name1, name2)
    else:
        raise TypeError("can't add new attribute")
