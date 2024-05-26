#!/usr/bin/python3

def roman_to_int(roman_string):
    rdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    k, summy = 0, 0
    lst = list(roman_string)
    while (k < len(lst) - 1):
        if rdic[lst[k]] >= rdic[lst[k + 1]]:
            summy += rdic[lst[k]]
        else:
            summy += rdic[lst[k+1]] - rdic[lst[k]]
        k += 1
    if rdic[lst[k-1]] >= rdic[lst[k]]:
        summy += rdic[lst[k]]
    return summy
