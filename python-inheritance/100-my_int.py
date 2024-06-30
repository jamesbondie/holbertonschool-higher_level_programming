#!/usr/bin/python3
"""IS DOCUMENTED"""


class MyInt(int):
    """IS DOCUMENTED"""
    def __eq__(self, var):
        return super().__ne__(var)

    def __ne__(self, var):
        return super().__eq__(var)
