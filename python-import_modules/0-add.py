#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    if (b >= 0):
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    else:
        print("{0} + {1} = {2}".format(a, b, a - b))
