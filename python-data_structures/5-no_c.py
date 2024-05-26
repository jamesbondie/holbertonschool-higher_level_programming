#!/usr/bin/python3

def no_c(my_string):
    i = 0
    my_str = ''
    while (i < len(my_string) - 1):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            my_str = my_string[0:i] + my_string[(i + 1):]
        i += 1
    return my_str
