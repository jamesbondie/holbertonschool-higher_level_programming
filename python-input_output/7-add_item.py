#!/usr/bin/python3

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
x = save_to_json_file()
i = 0
while i < len(sys.argv):
    x.append(sys.argv[i])
    i += 1
load_from_json_file()
