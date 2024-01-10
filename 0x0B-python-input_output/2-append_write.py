#!/usr/bin/python3
"""Module to append a file"""


def append_write(filename="", text=""):
    """Append `text` to `filename`

    Args:
        filename (str): file to write to
        text (str): text to write to `filenmae`

    Returns: the number of characters written
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
