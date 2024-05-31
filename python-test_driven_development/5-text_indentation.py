#!/usr/bin/python3
"""This is our module"""


def text_indentation(text):
    """This is function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in [".", "?", ":"]:
        text = text.replace(i, i + '\n\n')
    for i in text.split('\n'):
        print(i.strip())
