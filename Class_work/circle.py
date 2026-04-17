# Program to calculate area and perimeter (circumference) of a circle

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius * radius
perimeter = 2 * math.pi * radius   # circumference

print("Area of circle =", area)
print("Perimeter of circle =", perimeter)