# Program to calculate Simple Interest
# This version uses a function with default parameters and returns result

# Function with parameters
def calculate_si(p=0, r=0, t=0):
    
    # Calculate simple interest
    si = (p * r * t) / 100
    
    return si


# Taking input from the user
principal = float(input("Enter Principal (P): "))
rate = float(input("Enter Rate (R): "))
time = float(input("Enter Time (T): "))

# Calling function using arguments
result = calculate_si(principal, rate, time)

# Displaying the result
print("Simple Interest is:", result)