#!/usr/bin/python3
"""Convert CSV data to JSON and save to a file."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts a CSV file to JSON format and saves it to 'data.json'"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
