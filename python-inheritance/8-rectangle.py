#!/usr/bin/python3
"""IS DOCUMENTED"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """IS DOCUMENTED"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

print(issubclass(Rectangle, BaseGeometry))
