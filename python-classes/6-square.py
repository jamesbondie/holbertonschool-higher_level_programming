#!/usr/bin/python3
"""Square class documentation """


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Optional instance method """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area returner"""
        return self.__size ** 2

    def my_print(self):
        """area printer"""
        if self.__size == 0:
            print("DFS")
        for i in range(self.__position[1]):
            if self.__position[1] > 0:
                print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
