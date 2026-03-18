# Program to calculate electricity bill
# This version uses a dictionary for rates (different logic)

# Taking input from the user
units = int(input("Enter units consumed: "))

# Dictionary to store rates
rates = {
    "low": 4,     # up to 100 units
    "medium": 6,  # 101–200 units
    "high": 9     # above 200 units
}

# Determining category and calculating bill
if units <= 100:
    bill = units * rates["low"]

elif units <= 200:
    bill = units * rates["medium"]

else:
    bill = units * rates["high"]

# Displaying the result
print("Total electricity bill amount is:", bill)