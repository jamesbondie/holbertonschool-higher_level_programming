#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 123:
        for i in range(97, 123):
            if (c == chr(i)):
                return True
            else:
                return False
