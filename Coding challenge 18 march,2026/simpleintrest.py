# Program to calculate Simple Interest using a function

# Creating a function to calculate simple interest
def calculate_si(P, R, T):
    # Formula for Simple Interest
    SI = (P * R * T) / 100
    return SI


# Taking input from the user
P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of interest (R): "))
T = float(input("Enter Time in years (T): "))

# Calling the function
simple_interest = calculate_si(P, R, T)

# Displaying the result
print("Simple Interest is:", simple_interest)