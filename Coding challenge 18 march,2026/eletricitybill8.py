# Program to calculate electricity bill
# This version uses recursion (different logic)

# Recursive function to calculate bill
def calculate_bill(units):
    
    # Base case
    if units == 0:
        return 0
    
    # Apply rate based on current unit
    if units <= 100:
        return 5 + calculate_bill(units - 1)
    elif units <= 200:
        return 7 + calculate_bill(units - 1)
    else:
        return 10 + calculate_bill(units - 1)


# Taking input from user
units = int(input("Enter units consumed: "))

# Calling recursive function
total_bill = calculate_bill(units)

# Displaying result
print("Total electricity bill amount is:", total_bill)