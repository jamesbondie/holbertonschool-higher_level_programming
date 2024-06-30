#!/usr/bin/python3
"""Square module."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize with size."""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __lt__(self, other):
        """Check if this square is less than another square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another square."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Check if this square is equal to another square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if this square is not equal to another square."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if this square is greater than another square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another square."""
        return self.area() >= other.area()

    def __repr__(self):
        """Return the string representation of the square."""
        return f"Square(size={self.__size})"
