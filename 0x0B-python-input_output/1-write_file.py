#!/usr/bin/python3
"""write a string to a file"""


def write_file(filename="", text=""):
     """Opens a file up for read and writes text
     
     Args:
          filename (str): file to open
          text (str): text to be written to file
     """
     with open(filename, 'r+', encoding='utf8') as f:
          f.write(text)
