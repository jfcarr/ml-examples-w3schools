#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# x-axis data:
x = numpy.random.normal(5.0, 1.0, 1000)

# y-axis data:
y = numpy.random.normal(10.0, 2.0, 1000)

# Generate scatter plot:
plt.scatter(x, y)
plt.show()