#!/usr/bin/python3
"""IS DOCUMENTED"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """IS DOCUMENTED"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return super().area()
