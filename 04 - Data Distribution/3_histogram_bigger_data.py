#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# Generate an data set with 100000 random numbers:
x = numpy.random.uniform(0.0, 5.0, 100000)

# Then, plot a histogram with it:
plt.hist(x, 100)
plt.show()