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
