#!/usr/bin/python3
"""IS DOCUMENTED"""


class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last.name
        self.age = age

    def to_json(self, attrs=None):
        x = 0
        for i in attrs:
            if type(i) is not str:
                del attrs[x]
                x += 1
        return vars(attrs)
