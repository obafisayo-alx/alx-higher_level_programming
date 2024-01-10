#!/usr/bin/python3
"""Module to implement class and method to serialize itself"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, (list, tuple)):
            return self.__dict__.copy()
        else:
            res = {k: v for k, v in filter(lambda x: x[0] in attrs,
                                           self.__dict__.items())}
            return res
