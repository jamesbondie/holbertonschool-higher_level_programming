#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = []
    for key, value in a_dictionary.items():
        x.append(key)
    x.sort()
    for i in x:
        print("{}: {}".format(i, a_dictionary.get(i)))
