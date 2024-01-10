#!/usr/bin/python3
"""reading and printing text files"""


def read_file(filename=""):
    """opens a file for read only
     
    Args:
        filename (str): file to open
    """
    with open(filename, 'r', encoding='utf-8') as myfile:
        read_data = myfile.read()
        print(read_data, end="")
