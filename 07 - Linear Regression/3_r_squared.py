#!/usr/bin/python3

from scipy import stats

# How well does my data fit in a linear regression?
# (Ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)