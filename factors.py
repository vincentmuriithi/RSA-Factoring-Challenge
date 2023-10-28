#!/usr/bin/python3

import math

# Read the file and process each line
with open('tests/test00', 'r') as file:
    lines = file.readlines()

for line in lines:
    number = int(line.strip())
    factors = []
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            factors.append((i, number // i))
    for factor in factors:
        print(f"{number}={factor[0]}*{factor[1]}")
