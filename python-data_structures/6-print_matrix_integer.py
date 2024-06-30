#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    j = 0
    for i in matrix:
        for j in i:
            if (j == i[-1]):
                print(j)
                j += 1
            else:
                print("{:d} ".format(j), end="")
                j += 1
    if (j == 0):
        print("")
