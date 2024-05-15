#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastdigit = (abs(number) % 10) * -1
else:
    lastdigit = number % 10
if lastdigit > 5:
    str2 = "and is greater than 5"
elif lastdigit == 0:
    str2 = "and is 0"
else:
    str2 = "and is less than 6 and not 0"
print(f'Last digit of {number} is {lastdigit} {str2}')
