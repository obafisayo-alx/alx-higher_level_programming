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

        Raise:
            TypeError: If `width`, `height`, `x`, or `y` are not ints.
            ValueError: If `width` or `height` are <= 0, or `x` or `y`
                are < 0.
        """
        super().__init__(id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter/setter for width property.

        Raises:
            TypeError: If `width` is not an int.
            ValueError: If `width` is <= 0.

        Returns: value associated with `width`
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for `width`."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter for height property.

        Raises:
            TypeError: If `height` is not an int.
            ValueError: If `height` is <= 0.

        Returns: value associated with `height`
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for `height`."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter/setter for x (offset) property.

        Raises:
            TypeError: If `x` is not an int.
            ValueError: If `x` is < 0.

        Returns: value associated with `x`
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for `x` (offset)."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter/setter for y (offset) property.

        Raises:
            TypeError: If `y` is not an int.
            ValueError: If `y` is < 0.

        Returns: value associated with `y`
        """
        return self.__y
