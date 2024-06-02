#!/usr/bin/python3
"""IS DOCUMENTED"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """IS DOCUMENTED"""
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
