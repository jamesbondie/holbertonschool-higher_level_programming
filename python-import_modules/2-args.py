#!/usr/bin/python3
import sys

if (len(sys.argv) - 1 == 0):
    print(f"{len(sys.argv) - 1} arguments.")
else:
    if (len(sys.argv) - 1 ) % 2 == 0:
        print(f"{len(sys.argv) - 1} arguments:")
    else:
        print(f"{len(sys.argv) - 1} argument:")

i = 1
while ( i < len(sys.argv )):
    print(f"{i}: {sys.argv[i]}")
    i += 1