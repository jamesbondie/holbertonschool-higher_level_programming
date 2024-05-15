#!/usr/bin/python3
import sys

i = 1
result = 0
while (i < len(sys.argv)):
    result += int(sys.argv[i])
    i += 1
print(result)