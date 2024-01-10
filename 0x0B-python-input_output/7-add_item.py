#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a JSON file."""


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    # Load existing data from add_item.json
    existing_data = load_from_json_file('add_item.json')

    # Add command-line arguments to the existing data
    updated_data = existing_data + argv[1:]

    # Save the updated data to add_item.json
    save_to_json_file(updated_data, 'add_item.json')
