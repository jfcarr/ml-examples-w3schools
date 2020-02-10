#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

# x-axis data:
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]

# y-axis data:
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# Create polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Specify how the line will display:
myline = numpy.linspace(1, 22, 100)

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))

# Display the diagram:
plt.show()