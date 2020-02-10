#!/usr/bin/python3

import math
import numpy

speed = [32,111,138,28,59,77,97]

# The numpy var() method finds the variance:
x = numpy.var(speed)

print(f"The variance is {x}")

# Using variance to derive the standard deviation:
standard_deviation = math.sqrt(x)
print(f"The standard deviation is {standard_deviation}")

# ...and back again:
variance = standard_deviation * standard_deviation
print(f"The variance (from standard deviation) is {variance}")