#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    lenn = 0
    for i in range(x):
        if type(my_list[i]) is int:
            try:
                print("{:d}".format(my_list[i]), end="")
                lenn += 1
            except:
                print(end="")
        else:
            print(end="")
    return lenn
