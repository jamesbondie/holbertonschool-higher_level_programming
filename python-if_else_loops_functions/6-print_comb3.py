#!/usr/bin/python3

for i in range(0, 10):
    if (i // 10 != i % 10):
        print("{:02d}, ".format(i), end="")

for i in range(10, 88):
    if (i // 10 < i % 10):
        print("{:02d}, ".format(i), end="")
print(89)
