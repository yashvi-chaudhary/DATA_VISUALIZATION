# Program to calculate Simple Interest
# This version uses user-defined function with input inside function

# Defining the function
def calculate_si():
    
    # Taking input inside the function
    P = float(input("Enter Principal (P): "))
    R = float(input("Enter Rate (R): "))
    T = float(input("Enter Time (T): "))
    
    # Calculating simple interest
    SI = (P * R * T) / 100
    
    # Returning the result
    return SI


# Calling the function and storing result
result = calculate_si()

# Displaying the result
print("Simple Interest is:", result)