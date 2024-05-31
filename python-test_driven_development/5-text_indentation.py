#!/usr/bin/python3
"""This is our module"""


def text_indentation(text):
    """This is our function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    y = text.replace(" \\", "")
    listr = [". ", ": ", "? "]
    for i in listr:
        y = y.replace(i, i[0:1] + "\n\n")
    print(y)
