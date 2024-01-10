#!/usr/bin/python3
"""reading and printing text files"""


def read_file(filename=""):
    """opens a file for read only
     
    Args:
        filename (str): file to open
    """
    with open(filename, 'r', encoding='utf8') as myfile:
        print(myfile.read(), end="")
