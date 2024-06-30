#!/usr/bin/python3
import sys
if __name__ == '__main__':

    if (len(sys.argv) - 1 == 0):
        print(f"{len(sys.argv) - 1} arguments.")
    else:
        if len(sys.argv) - 1 == 1:
            print(f"{len(sys.argv) - 1} argument:")
        else:
            print(f"{len(sys.argv) - 1} arguments:")

    i = 1
    while (i < len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
        i += 1
