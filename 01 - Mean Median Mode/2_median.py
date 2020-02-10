#!/usr/bin/python3

import numpy

# Given a list of values:
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# numpy.median calculates the median, which is the value in the middle, after sorting:
x = numpy.median(speed)

print(f"Median of first list is {x}")

# If the list count is even-numbered, resulting in two values being in the middle, those
# values are added together, and the result is divided by 2:

even_count_list = [1,2,3,4,5,6]
x = numpy.median(even_count_list)

print(f"Median of second list is {x}")
