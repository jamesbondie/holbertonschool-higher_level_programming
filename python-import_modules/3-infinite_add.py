#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = 1
    result = 0
    while (i < len(sys.argv)):
        result += int(sys.argv[i])
        i += 1
    print(result)
