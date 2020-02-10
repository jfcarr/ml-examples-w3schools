#!/usr/bin/python3

import pandas
from sklearn import linear_model

# Use Pandas module to read csv files and return a DataFrame object:
df = pandas.read_csv("cars.csv")

# Make a list of the independent values and call this variable X:
X = df[['Weight', 'Volume']]

# Put the dependent values in a variable called y:
y = df['CO2']

# (It is common to name the list of independent values with a upper case X, and the list of dependent values with a lower case y.)

# Use the fit() method to fill the regression object with data that describes the relationship:
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict the CO2 emission of a car where the weight is 3300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[3300, 1300]])

print(f"Predicted CO2 is {float(predictedCO2)}")