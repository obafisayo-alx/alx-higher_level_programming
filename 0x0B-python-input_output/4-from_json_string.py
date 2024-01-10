#!/usr/bin/python3
"""object represented as json string"""
import json


def from_json_string(my_str):
    """convert json string to object

    Args:
        my_str (str): json string to be deserialized

    Returns: object represented by `my_str`
    """
    return json.loads(my_str)
