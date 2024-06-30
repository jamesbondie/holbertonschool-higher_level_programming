#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if x == 0:
            print()
            return x
        lenn, j = 0, 0
        strr = ""
        for i in my_list:
            strr += str(i)
        for i in strr:
            if x == int(i):
                strr = strr[:x]
        for i in strr:
            lenn += 1
        print(strr)
        return lenn

    except TypeError:
        print("hellooo")
