#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if type(value) is int:
            print(value)
            return True



    except:
        return False
