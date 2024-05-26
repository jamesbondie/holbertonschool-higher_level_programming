#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    i = 0
    x = len(my_list) - 1
    while (i <= x):
        print("{:d}".format(my_list[x]))
        x -= 1
