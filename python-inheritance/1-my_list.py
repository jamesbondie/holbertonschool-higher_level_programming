#!/usr/bin/python3
"""IS DOCUMENTED"""


class MyList(list):
    """IS DOCUMENTED"""
    def print_sorted(self):
        y = sorted(self.copy())
        print(y)
        return y
