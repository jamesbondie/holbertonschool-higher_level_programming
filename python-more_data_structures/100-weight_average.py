#!/usr/bin/python3

def weight_average(my_list=[]):
    summy = 0
    divider = 0
    x = 0
    if len(my_list) == 0:
        return 0
    while (x < len(my_list)):
        summy += my_list[x][0] * my_list[x][1]
        divider += my_list[x][1]
        x += 1
    return summy/divider
