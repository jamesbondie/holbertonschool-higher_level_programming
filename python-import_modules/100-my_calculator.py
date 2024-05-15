#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if (len(sys.argv) - 1 != 3):
  print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
  exit(1)
else:
  if sys.argv[2] == "+":
    print(f"{sys.argv[1]} + {sys.argv[3]} = {add(int(sys.argv[1]), int(sys.argv[3]))}")
  elif sys.argv[2] == "-":
    print(f"{sys.argv[1]} - {sys.argv[3]} = {sub(int(sys.argv[1]), int(sys.argv[3]))}")
  elif sys.argv[2] == "*":
    print(f"{sys.argv[1]} * {sys.argv[3]} = {mul(int(sys.argv[1]), int(sys.argv[3]))}")
  elif sys.argv[2] == "/":
    print(f"{sys.argv[1]} / {sys.argv[3]} = {div(int(sys.argv[1]), int(sys.argv[3]))}")
  else:
    print("Unknown operator. Available operators: +, -, * and /\n")
    exit(1)