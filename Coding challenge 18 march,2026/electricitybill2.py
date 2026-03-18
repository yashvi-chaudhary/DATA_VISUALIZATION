# Program to calculate electricity bill using a different logic

# Taking input from the user
units = int(input("Enter the number of units consumed: "))

# Rate per unit based on range
rate = 0

if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
else:
    rate = 9

# Calculating bill
bill = units * rate

# Displaying result
print("Total electricity bill:", bill)