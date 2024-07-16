import logging
import sys
from jinja2 import Template
import os

def generate_invitations(template, attendees):
    if isinstance(template, str) and isinstance(attendees, list):
        
        for i in attendees:
            if isinstance(i, dict):
                pass
            else:
                print("Invalid input type")
                return
    else:
        print("Invalid input type")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return
        
    index = 1
    for james in attendees:
        for key in james.keys():
            if james[key] is None:
                james[key] = "{}: N/A".format(key)
            

        processed = template.format(**james)
        if not os.path.exists('output_{}.txt'.format(index)):
            with open('output_{}.txt'.format(index), 'w') as f:
                f.write(processed)
        else:
            print("The output already exists.")
        index += 1