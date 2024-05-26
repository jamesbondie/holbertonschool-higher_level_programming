#!/usr/bin/python3

class Square:
    square = 0
    


    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        if (self.__size == 0):
            print()
        while i < self.__size:
            k = 0
            while k < self.__size:
                print("#", end="")
                k += 1 
            i += 1
            print()

