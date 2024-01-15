#!/usr/bin/python3
"""Module contains a subclass Rectangle which inherits from base"""
from models.base import Base


class Rectangle(Base):
    """creates an instance for a rectangle which inherits the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize new instance of rectangle with width, height and offsets

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): width offset for drawing rectangle
            y (int): height offset for drawing rectangle
            id: identifier for instance. If None, then object count
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """width property getter method
            Returns: value assigned with width
            """
            return self.__width
        
        @width.setter
        def width(self, value):
            """width setter method
            Args:
                value (int): value to set the width value to
            """
            self.__width = value

        @property
        def height(self):
            """height property getter method
            Returns: value assigned with height
            """
            return self.__height
        
        @height.setter
        def height(self, value):
            """height setter method
            Args:
                value (int): value to set the height value to
            """
            self.__height = value

        @property
        def x(self):
            """x property getter method
            Returns: value assigned with x
            """
            return self.__x
        
        @x.setter
        def x(self, value):
            """x setter method
            Args:
                value (int): value to set the x value to
            """
            self.__x = value

        @property
        def y(self):
            """y property getter method
            Returns: value assigned with y
            """
            return self.__y
        
        @y.setter
        def y(self, value):
            """y setter method
            Args:
                value (int): value to set the y value to
            """
            self.__y = value
