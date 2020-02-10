#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# Generate a uniformly distributed set of random data (250 elements):
x = numpy.random.uniform(0.0, 5.0, 250)

# Then, plot a histogram with it:
plt.hist(x, 5)
plt.show()
