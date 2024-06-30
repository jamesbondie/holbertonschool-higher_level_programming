#!/usr/bin/python3
"""THIS MODULE CONTAINS CLASSES TASKS"""


class Rectangle:
    """THIS CLASS REPRESENTS RECTANGLE"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        str1 = ""
        for i in range(self.height):
            for k in range(self.width):
                str1 += "#"
            if not i == self.height - 1:
                str1 += "\n"
        return str1

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
