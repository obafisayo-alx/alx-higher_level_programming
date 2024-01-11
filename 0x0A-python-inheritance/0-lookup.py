#!/usr/bin/python3
"""Creates a list of available attributes and methods of an object"""


def lookup(obj):
    """returns list of attributes and methods of objects"""
    return dir(obj)
