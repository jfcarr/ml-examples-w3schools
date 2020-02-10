#!/usr/bin/python3

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)
print(f"75th percentile -> 75% of the group is younger than {int(x)}")

x = numpy.percentile(ages, 10)
print(f"10th percentile -> 10% of the group is younger than {int(x)}")

x = numpy.percentile(ages, 90)
print(f"90th percentile -> 90% of the group is younger than {int(x)}")
