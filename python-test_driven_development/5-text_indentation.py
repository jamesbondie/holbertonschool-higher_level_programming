#!/usr/bin/python3
"""This is our module"""


def text_indentation(text):
    """This is our function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in [". ", ": ", "? "]:
        text = text.replace("  ", "").replace(i, i[0])
    for i in text:
        print(i, end="")
        if i == "." or i == ":" or i == "?":
            print('\n')
