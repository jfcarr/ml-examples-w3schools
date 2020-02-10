#!/usr/bin/python3

import numpy

# Given a list of values:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# numpy.mean calculates the mean (average) value:
x = numpy.mean(speed)

print(f"The average is {x}")
