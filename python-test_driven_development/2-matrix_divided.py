#!/usr/bin/python3
"""This is our module"""
def matrix_divided(matrix, div):
    """This is our function"""
    for k in matrix:
        for i in k:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = list(map(lambda x: list(map(lambda z: z/div, x)), matrix))
    rounded_new_matrix = list(map(lambda x: list(map(lambda c: round(c, 2), x)), new_matrix))
    return rounded_new_matrix
