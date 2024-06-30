#!/usr/bin/python3
"""IS DOCUMENTED"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
lisst = []
try:
    x = load_from_json_file("add_item.json")
    for i in x:
        lisst.append(i)
except Exception:
    pass
i = 1
while i < len(sys.argv):
    lisst.append(sys.argv[i])
    i += 1
save_to_json_file(lisst, "add_item.json")
