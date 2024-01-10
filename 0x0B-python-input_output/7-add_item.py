#!/usr/bin/python3
"""Add all arguments to a list and save its JSON encoding to a file"""


from sys import argv

save_to_json = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json = __import__('6-load_from_json_file.py').load_from_json_file

FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        save_to_json(load_from_json(FILENAME) + argv[1:], FILENAME)
    except (FileNotFoundError, ValueError):
        save_to_json(argv[1:], FILENAME)
