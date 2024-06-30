#!/usr/bin/python3
"""IS DOCUMENTED"""


class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)

        x = {}
        for i in attrs:
            if i in vars(self):
                x[i] = vars(self)[i]
        return x

    def reload_from_json(self, json):
        for i in json:
            vars(self)[i] = json[i]
