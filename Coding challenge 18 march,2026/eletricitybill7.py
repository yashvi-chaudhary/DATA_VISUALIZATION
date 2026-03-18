# Program to calculate electricity bill
# This version uses a function and adds a fixed charge

# Function to calculate bill
def calculate_bill(units):
    
    # Fixed charge (extra logic added)
    fixed_charge = 50
    
    # Variable bill calculation
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = units * 7
    else:
        bill = units * 10
    
    # Adding fixed charge
    total = bill + fixed_charge
    
    return total


# Taking input from user
units = int(input("Enter units consumed: "))

# Calling function
total_bill = calculate_bill(units)

# Displaying result
print("Total electricity bill amount is:", total_bill)