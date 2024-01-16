#!/usr/bin/python3
"""Module contains a base class to be used by other subclasses"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to serialize list of dictionary objects into json.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into json
                representation.

        Returns: Json string representation of `list_dictionaries`.

        Raises: Any errors encounterd during serialization.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to convert `list_objs` to json string and
        save in file with name '<class name>.json'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any errors encountered during serialization and I/O.
        """
        if not list_objs:
            list_objs = []
        with open("{}.json".format(cls.__name__), 'w') as jf:
            jf.write(cls.to_json_string([obj.to_dictionary() for
                                         obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Static method to deserialize json string into python objects.

        Args:
            json_string (str): String representation of objects.

        Returns: Python objects represented by `json_string`.

        Raises: Any errors encountered during serialization.
        """
        if json_string == "" or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method to create new instance directly from the class. Mainly
        for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for new instance.

        Returns: New instance of class from which `create` was called.

        Raises: Errors delegated to subclasses of Base which call this
            method.
        """
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        if not hasattr(dictionary, "keys") or not callable(dictionary.keys):
            dictionary = {}
        c.update(**dictionary)
        return c
