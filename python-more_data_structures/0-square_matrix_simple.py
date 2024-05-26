#!/usr/bin/python3
import copy
def square_matrix_simple(matrix=[]):
    new_matrix = copy.deepcopy(matrix)
    i, j, k = 0, 0, 0
    while (i < len(matrix)):
        k = 0
        for j in matrix[i]:
            new_matrix[i][k] = j**2
            k += 1
        i += 1
    return new_matrix
