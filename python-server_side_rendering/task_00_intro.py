#!/usr/bin/python3
from os import exists

"""Module that defines a function for generating invitations"""
def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    
    if not template.strip():
        print("Error: 'template' cannot be empty.")
        return
    
    if not isinstance(attendees, dict):
        print("Error: attendees must be a list of dictionaries")
        return
    
    if not attendees:
        print("Error: 'attendees' list cannot be empty.")
        return

    for index, attendee in enumerate(attendees_list, start=1):
        template_schema = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            placeholder = "{" + f"{key}" + "}"
            value = attendee.get(key) or "N/A"
            template_schema = template_schema.replace(placeholder, value)
        if not exists(f"output_{index}.txt"):
            with open(f"output_{index}.txt", "w") as file:
                file.write(template_schema)
        else:
            print("ERROR: file already exists")