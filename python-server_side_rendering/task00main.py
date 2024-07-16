# Main file content
from task_00_intro import generate_invitations

file_path = '/home/9095@holbertonstudents.com/holbertonschool-higher_level_programming/python-server_side_rendering/template.txt'

# Read the template from a file
with open(file_path, 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)