#!/usr/bin/python3
""" This is a class for a rectangle """


class Rectangle:
    """ The init method initializes the rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """gets height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value"""
        try:
            if not isinstance(value, int):
                raise TypeError
            if value < 0:
                raise ValueError
            self.__height = value
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value"""
        try:
            if not isinstance(value, int):
                raise TypeError
            if value < 0:
                raise ValueError
            self.__width = value
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
