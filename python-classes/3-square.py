#!/usr/bin/python3
"""Square module."""


class Square:
    """Represents a square."""
    square = 0

    def __init__(self, size=0):
        """Initialize with size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
