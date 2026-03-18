# Program to calculate simple interest using a function

# Defining the function
def simple_interest(P, R, T):
    interest = (P * R * T) / 100
    return interest

# Taking input from user
P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate (R): "))
T = float(input("Enter Time (T): "))

# Calling the function
result = simple_interest(P, R, T)

# Printing the result
print("Simple Interest =", result)