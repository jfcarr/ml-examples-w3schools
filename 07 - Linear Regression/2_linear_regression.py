#!/usr/bin/python3

import matplotlib.pyplot as plt
from scipy import stats

# x-axis data:
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

# y-axis data:
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Calculate key linear regression values:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Calculate position of x value on y-axis:
def myfunc(x):
  return slope * x + intercept

# Generate data model (array with new values for the y-axis):
mymodel = list(map(myfunc, x))

# Generate scatter plot:
plt.scatter(x, y)

# Generate linear regression line:
plt.plot(x, mymodel)

# Display the diagram:
plt.show()