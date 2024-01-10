#!/usr/bin/python3
"""Module to implement class and method to serialize itself"""


class Student:
    """A class to rep student and methods to create json strings"""
    def __init__(self, first_name, last_name, age):
        """initialize student instance with first, last names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """creates copy of attributes for use in json string"""
        if attrs is None or not isinstance(attrs, (list, tuple)):
            return self.__dict__.copy()
        else:
            res = {k: v for k, v in filter(lambda x: x[0] in attrs,
                                           self.__dict__.items())}
            return res

    def reload_from_json(self, json):
        """Use serialized version of `Student` instance to update `self`

        Recreate instance from previously serialized `Student` instance.
        """
        if not isinstance(json, dict):
            raise ValueError("Input must be a dictionary")
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
    # alternatively,
    # self.__dict__.update(json) - this does the same thing as the code above
