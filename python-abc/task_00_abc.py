#!/usr/bin/python3
"""IS DOCUMENTED"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """IS DOCUMENTED"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """IS DOCUMENTED"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """IS DOCUMENTED"""
    def sound(self):
        return "Meow"
