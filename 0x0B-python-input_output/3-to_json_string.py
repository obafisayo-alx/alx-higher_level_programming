#!/usr/bin/python3
"""json represenntation of an object"""
import json


def to_json_string(my_obj):
    """converts object to json string

    Args:
        object (obj): object to be serialized `my_obj`

    Returns: json representation of the object
    """
    return json.dumps(my_obj)
