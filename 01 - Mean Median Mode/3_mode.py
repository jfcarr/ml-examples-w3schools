#!/usr/bin/python3

from scipy import stats

# Given a list of values:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# stats.mode calculates the mode, which is the value that appears the most:
x = stats.mode(speed)

print(f"The mode value is {float(x[0])}")
