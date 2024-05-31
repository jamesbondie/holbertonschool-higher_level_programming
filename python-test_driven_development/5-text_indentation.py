#!/usr/bin/python3
"""This is our module"""
def text_indentation(text):
    """This is our function"""
    text2 = ""
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            text2 = text2 + text[:i]
            text2 = text2 + ""
        else:
            print(text[i], end="")
        print(text2)
