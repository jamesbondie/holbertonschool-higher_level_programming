#!/usr/bin/python3
"""IMPORTING XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serializing to xml"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        sub = ET.SubElement(root, key)
        sub.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """deserializing"""
    tree = ET.parse(filename)
    root = tree.getroot()
    deserialized_dict = {}
    for element in root:
        deserialized_dict[element.tag] = element.text
    return deserialized_dict
