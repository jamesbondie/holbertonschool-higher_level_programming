#!/usr/bin/python3
number = 3.14159
try:
    print(f'Float: {"%.2f" % number}')
except ValueError:
    print("Unknown format code 'f' for object of type 'str'")
