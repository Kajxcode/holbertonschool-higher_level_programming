#!/usr/bin/python3
"""Module for serializing and deserializing dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, str(key))
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True

    except (ET.ParseError, OSError):
        return False


def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            text = child.text
            if text is None:
                result[child.tag] = None
                continue

            if text.lower() == "true":
                result[child.tag] = True
            elif text.lower() == "false":
                result[child.tag] = False
            elif text.isdigit():
                result[child.tag] = int(text)
            else:
                try:
                    result[child.tag] = float(text)
                except ValueError:
                    result[child.tag] = text
        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None
