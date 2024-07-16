import logging
import sys
from jinja2 import Template

def generate_invitations(template, attendees):
    if isinstance(template, str) and isinstance(attendees, list):
        
        for i in attendees:
            if isinstance(i, dict):
                pass
            else:
                logging.error("Invalid input type")
                sys.exit(1)
    else:
        logging.error("Invalid input type")
        sys.exit(1)

    if template is None:
        logging.error("Template is empty, no output files generated.")
        sys.exit(1)

    if attendees is None:
        logging.error("No data provided, no output files generated.")
        sys.exit(1)
        
    index = 1
    for james in attendees:
        for key in james.keys():
            if james[key] is None:
                james[key] = "N/A"
            

        processed = template.format(**james)
        with open('output_{}.txt'.format(index), 'w') as f:
            f.write(processed)
        index += 1
        print(index)

    
