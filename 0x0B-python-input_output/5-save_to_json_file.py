#!/usr/bin/python3
"""Object to text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """convert an object `my_obj` to json and save to `filename`

    Args:
        my_obj (obj): object file to be serialzed
        filename (str): file to store json representation

    Returns: saves json representation to file
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(json.dumps(my_obj))
