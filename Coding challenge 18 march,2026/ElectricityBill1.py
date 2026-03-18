# Program to calculate electricity bill based on units consumed
# This version uses a slightly different logic from the previous program

# Taking input from the user
units = float(input("Enter the number of units consumed: "))

# Initializing bill variable
bill = 0

# Using different slab logic
# Up to 100 units -> Rs 5 per unit
# 101 to 200 units -> Rs 8 per unit
# Above 200 units -> Rs 10 per unit

if units > 200:
    bill = units * 10
elif units > 100:
    bill = units * 8
else:
    bill = units * 5