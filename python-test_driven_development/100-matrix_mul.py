#!/usr/bin/python3
"""This module is for multiplication of matrices"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    

    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError("m_a must be a list of lists")
        if not isinstance(m_a[i], (int, float)):
            raise TypeError("m_a should contain only integers or floats")
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    

    for i in range(len(m_b)):
        if not isinstance(m_b[i], list):
            raise TypeError("m_b must be a list of lists")
        if not isinstance(m_b[i], (int, float)):
            raise TypeError("m_b should contain only integers or floats")
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")


    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in m_a:

