#!/usr/bin/python3
"""IS DOCUMENTED"""


def matrix_mul(m_a, m_b):
    """IS DOCUMENTED"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if not any(m_a):
        raise ValueError("m_a can't be empty")
    if not any(m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rows_a, cols_a = len(m_a), len(m_a[0])
    rows_b, cols_b = len(m_b), len(m_b[0])
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
