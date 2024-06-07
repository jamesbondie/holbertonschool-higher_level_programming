#!/usr/bin/python3
"""IS DOCUMENTED"""


def pascal_triangle(n):
    """finally i managed to write it with my dump variables"""
    if n <= 0:
        return []
    main_list = [[1], [1, 1]]
    i = 1
    new_list = []
    a = 2
    k = 0
    while a < n:
        b = 0
        new_list = []
        new_list.append(1)
        k = 0
        while b < a - 1:
            x = main_list[a - 1][k] + main_list[a - 1][k + 1]
            new_list.append(x)
            if (k == len(main_list[a - 1]) - 2):
                pass
            else:
                k += 1
            b += 1
        new_list.append(1)
        main_list.append(new_list)
        a += 1
    return main_list
