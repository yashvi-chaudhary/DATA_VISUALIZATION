# Program to calculate electricity bill
# This version uses a function with slab rates stored in a list

# Function to calculate bill
def calculate_bill(units):
    
    # Slab rates (unit limit, cost per unit)
    slabs = [(100, 5), (100, 7), (float('inf'), 10)]
    
    bill = 0
    
    # Loop through slabs
    for limit, rate in slabs:
        
        if units > limit:
            bill += limit * rate
            units -= limit
        else:
            bill += units * rate
            break
    
    return bill


# Taking input from user
units = int(input("Enter units consumed: "))

# Calling function
total_bill = calculate_bill(units)

# Displaying result
print("Total electricity bill amount is:", total_bill)