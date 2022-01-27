#!python3
"""
A population can be modeled by the following:
future population = (current population)*(1+r)^(time in years) 
Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
Calculate the expected future population

Enter the population: 25000000
Enter the rate of growth in percent: 2.1
Enter the number of days: 12
There will be 25017087 people after 12 days
"""
import math
x = input("Enter the population")
y = input("Enter the rate of growth in percent")
z = input("Enter the number of days")

z=int(z)
x=int(x)
y=str(y)
k = x*y/z
k = round(k)
k=str(k)


print("There will be " + k + " people after " + z + " days")