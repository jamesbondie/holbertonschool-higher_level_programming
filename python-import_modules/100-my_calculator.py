#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    if (len(argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    else:
        a = argv[1]
        b = argv[2]
        c = argv[3]
        if b == "+":
            print(f"{a} + {c} = {add(int(a), int(c))}")
        elif b == "-":
            print(f"{a} - {c} = {sub(int(a), int(c))}")
        elif b == "*":
            print(f"{a} * {c} = {mul(int(a), int(c))}")
        elif b == "/":
            print(f"{a} / {c} = {div(int(a), int(c))}")
        else:
            print("Unknown operator. Available operators: +, -, * and /\n")
            exit(1)
