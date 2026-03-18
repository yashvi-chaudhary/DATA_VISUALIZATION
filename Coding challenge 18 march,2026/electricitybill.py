# Program to calculate electricity bill based on units consumed

# Taking input from the user
units = float(input("Enter the number of units consumed: "))

# Initializing bill amount
bill = 0

# Calculating bill according to unit slabs
# Example slab system
# First 100 units = Rs 5 per unit
# Next 100 units = Rs 7 per unit
# Above 200 units = Rs 10 per unit

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Displaying the total bill amount
print("Total electricity bill is: Rs", bill)