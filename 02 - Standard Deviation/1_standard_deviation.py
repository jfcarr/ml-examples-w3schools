#!/usr/bin/python3

import numpy

speed = [86,87,88,86,87,85,86]

# The numpy std() method finds the standard deviation:
x = numpy.std(speed)

print(f"Low standard deviation value for numbers close to the mean: {x}")

disparate_range = [1,5,100,220,1000]
x = numpy.std(disparate_range)

print(f"High standard deviation value for numbers in a wider range from the mean: {x}")