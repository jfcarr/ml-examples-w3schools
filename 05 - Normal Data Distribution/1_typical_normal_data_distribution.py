#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# Generate a random data set, specifying a normal distribution:
x = numpy.random.normal(5.0, 1.0, 100000)

# Plot a histogram from the data:
plt.hist(x, 100)
plt.show()