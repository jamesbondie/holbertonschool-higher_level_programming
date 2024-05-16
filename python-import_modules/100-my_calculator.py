#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    a = argv[1]
    b = argv[2]
    c = argv[3]
    d = argv[4]
    if (len(argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    else:
        if argv[2] == "+":
            print(f"{a} + {c} = {add(int(a), int(sys.argv[3]))}")
        elif argv[2] == "-":
            print(f"{a} - {c} = {sub(int(a), int(sys.argv[3]))}")
        elif argv[2] == "*":
            print(f"{a} * {c} = {mul(int(a), int(argv[3]))}")
        elif argv[2] == "/":
            print(f"{a} / {c} = {div(int(a), int(argv[3]))}")
        else:
            print("Unknown operator. Available operators: +, -, * and /\n")
            exit(1)
