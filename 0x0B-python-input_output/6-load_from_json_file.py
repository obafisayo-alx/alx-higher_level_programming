#!/usr/bin/python3
"""creates object from json file"""
import json


def load_from_json_file(filename):
    """converts json file to object

    Args:
        filename (str): file that contains json string

    Returns: deserialized json file
    """
    with open(filename, 'r', encoding='utf8') as f:
        return json.loads(f.read())
