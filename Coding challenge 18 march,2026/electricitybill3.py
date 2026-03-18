# Program to calculate electricity bill
# This version uses a function and accumulates bill step-by-step (slab-wise)

# Function to calculate bill
def calculate_bill(units):
    
    bill = 0

    # First 100 units
    if units > 100:
        bill += 100 * 5
        units -= 100
    else:
        bill += units * 5
        return bill

    # Next 100 units
    if units > 100:
        bill += 100 * 7
        units -= 100
    else:
        bill += units * 7
        return bill

    # Remaining units
    bill += units * 10

    return bill