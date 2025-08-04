#!/usr/bin/python3
from os.path import exists

"""Module that defines a function for generating invitations"""
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    
    if not template.strip():
        print("Error: 'template' cannot be empty.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    
    if not attendees:
        print("Error: 'attendees' list cannot be empty.")
        return

    for index, attendee in enumerate(attendees, start=1):
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = f"{{{key}}}"
            value = attendee.get(key, "N/A")
            filled_template = filled_template.replace(placeholder, value)

    filename = f"output_{index}.txt"
    if not exists(filename):
        with open(filename, "w") as file:
                file.write(filled_template)
    else:
        print(f"ERROR: {filename} already exists")
