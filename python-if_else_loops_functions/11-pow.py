#!/usr/bin/python3


def pow(a, b):
    i = 0
    c = a
    if b > 0:
        i = 0
    while (i < b - 1):
        a *= c
        i += 1
    return a
    elif b == 0:
        return 1
    else:
        i = 0
        b = b * (-1)
        while (i < b - 1):
            a *= c
            i += 1
        return 1/a
