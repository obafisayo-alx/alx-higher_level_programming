#!/usr/bin/python3
"""Module containing subclass square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to represent a square derived from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize new square with width and height equal to `size`.

        Args:
            size (int): side lengths of square
            x (int): width offset for drawing square
            y (int): height offset for drawing square
            id: identifier for instance. If None, then object count.

        Raises:
            TypeError: If args are not int (or None for id)
            ValueError: If size is <= 0 or x, y and < 0 or id < 0
        """
        super().__init__(size, size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """getter for size instance field
        Uses width attribute from Rectangle parent to store `size`.

        raises:
            TypeError: if `size` is not an int
            ValueError: if `size` is less than or equal to 0

        Returns: value assigned to size
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size instance field"""
        setattr(self, "width", value)

    def __str__(self):
        """retuns string representation of square instance

        Example:
            >>> s = Square(3, 4, 8, 9) # --> (size, x, y, id)
            >>> print(s)
            [Square] (9) 4/8 - 3
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__,
            self.id,
            self.x, self.y,
            self.size
        )

    def update(self, *args, **kwargs):
        """Update Square instances with *args and **kwargs.
        Order of *args is 'id', 'size', 'x', 'y'. **kwargs can be in
        any order.

        Example:
            >>> s = Square(1)
            >>> args = [6]; kwargs = {"size": 4, "y": 3}
            >>> s.update(*args, **kwargs)
            >>> print(s)
            [Square] (6) 0/3 - 4
        """
        attrs = ["id", "size", "x", "y"]
        for attr, arg in zip(attrs, args):
            setattr(self, attr, arg)
        for k, v in kwargs.items():
            setattr(self, k, v)
