#!/usr/bin/python3

def is_same_class(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    if not isinstance(obj, a_class):
        return False
