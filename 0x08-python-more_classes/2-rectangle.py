#!/usr/bin/python3
"""Rectangle class

"""


class Rectangle:
    """create rectangle instances
    """
    def __init__(self, width=0, height=0):
        """initialzes the instances
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """gets height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height value
        """
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
        """gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width value
        """
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

    def area(self):
        """returns the area
        """
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter
        """
        if self.width == 0 and self.width == 0:
            return 0
        return (self.width + self.height) * 2
