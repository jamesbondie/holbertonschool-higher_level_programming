#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        k = [x**2 for x in i]
        new_matrix.append(k)
    return new_matrix
