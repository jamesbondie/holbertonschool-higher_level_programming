#!/usr/bin/python3
"""This is our integer added module"""


def add_integer(a, b=98):
    """This is our integer adder function"""
    
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a + 1 == a or b + 1 == b:
        raise OverflowError
    if type(a) is float:
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
