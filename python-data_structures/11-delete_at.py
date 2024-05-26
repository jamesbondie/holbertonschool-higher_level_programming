#!/usr/bin/python3

def delete_at(my_list=[], idx = 0):
    i = 0
    if (idx > len(my_list) - 1 or idx < 0):
        return my_list
    while (i < len(my_list) - 1):
        if (i == idx):
            del my_list[idx]
            return my_list
        i += 1
