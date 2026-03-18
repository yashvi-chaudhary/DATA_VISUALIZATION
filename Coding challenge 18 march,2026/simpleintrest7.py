# Program to calculate Simple Interest
# This version uses *args to accept multiple values (different logic)

# Function using *args
def calculate_si(*values):
    
    # Extracting values
    P = values[0]
    R = values[1]
    T = values[2]
    
    # Calculating simple interest
    SI = (P * R * T) / 100
    
    return SI


# Taking input from user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Calling function with arguments
result = calculate_si(p, r, t)

# Displaying result
print("Simple Interest is:", result)