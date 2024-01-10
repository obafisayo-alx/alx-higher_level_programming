#!/usr/bin/python3
"""Add all arguments to a list and save its JSON encoding to a file.

This script takes command-line arguments, loads existing data from a JSON file
if available, adds the command-line arguments to the existing data, and saves
the updated data back to the file in JSON format.

Usage:
    ./script_name.py arg1 arg2 ...

    Example:
    ./script_name.py apple banana orange

"""

from sys import argv

# Importing functions from external modules
save_to_json = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json = __import__('6-load_from_json_file.py').load_from_json_file

# File name for storing the data in JSON format
FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        # Try to load existing data from the JSON file
        existing_data = load_from_json(FILENAME)

        # Add command-line arguments to the existing data
        updated_data = existing_data + argv[1:]

        # Save the updated data to the JSON file
        save_to_json(updated_data, FILENAME)
    except (FileNotFoundError, ValueError):
        # If file not found or invalid JSON data, create a new file with
        # only the command-line arguments
        save_to_json(argv[1:], FILENAME)
