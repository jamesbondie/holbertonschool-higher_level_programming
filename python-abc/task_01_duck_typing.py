#!/usr/bin/python3
"""IS DOCUMENTED"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """IS DOCUMENTED"""
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Circle(Shape):
    """IS DOCUMENTED"""

    def __init__(self, radius):
        if radius < 0:
            radius *= -1
        self.radius = radius

    def area(self):
        return (self.radius**2) * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """IS DOCUMENTED"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """IS DOCUMENTED"""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
