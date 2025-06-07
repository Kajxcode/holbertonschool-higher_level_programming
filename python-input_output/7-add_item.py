#!/usr/bin/python3
"""adds all arguments to a Python list, then saves them to a JSON file"""


import sys
import json
import os

save_file = "add_item.json"

def load_from_json_file(filename):
    """Load JSON object from a file."""
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_to_json_file(my_obj, filename):
    """Save Python object to file as JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


my_list = load_from_json_file(save_file)


my_list.extend(sys.argv[1:])


save_to_json_file(my_list, save_file)
