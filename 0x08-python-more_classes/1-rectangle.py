#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """create rectangle instances"""
    def __init__(self, width=0, height=0):
        """initialzes the instances"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
