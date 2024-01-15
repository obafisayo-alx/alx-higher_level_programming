#!/usr/bin/python3
"""Module contains a base class to be used by other subclasses"""


class Base:
    """Base class to be subclassed by othe classes"""

    __nb_objects = 0
    """class field representing the count of base and sub-class instances"""

    def __init__(self, id=None):
        """initialize the base instance id

        Args:
            id (int): rep the base id, if none takes `__nb_objects` count
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
