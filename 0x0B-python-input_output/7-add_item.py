#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a JSON file."""


from sys import argv
from json import load, dump


def save_to_json_file(my_obj, filename):
    """Save object to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        dump(my_obj, file)


def load_from_json_file(filename):
    """Load object from a JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return load(file)
    except FileNotFoundError:
        return []


if __name__ == '__main__':
    # Load existing data from add_item.json
    existing_data = load_from_json_file('add_item.json')

    # Add command-line arguments to the existing data
    updated_data = existing_data + argv[1:]

    # Save the updated data to add_item.json
    save_to_json_file(updated_data, 'add_item.json')
