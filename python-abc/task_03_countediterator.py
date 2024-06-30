#!/usr/bin/env python3
"""IS DOCUMENTED"""


class CountedIterator():
    """IS DOCUMENTED"""

    def __init__(self, iterable):
        self.counter = 0
        self.iterable = iterable

    def get_count(self):
        return self.counter

    def __next__(self):
        if len(self.iterable) is self.counter:
            raise StopIteration
        self.counter += 1
        return self.iterable[self.counter - 1]
