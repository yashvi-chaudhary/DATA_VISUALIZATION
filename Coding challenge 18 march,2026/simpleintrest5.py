# Program to calculate Simple Interest
# This version uses lambda function (different logic)

# Defining a lambda function for simple interest
calculate_si = lambda p, r, t: (p * r * t) / 100

# Taking input from the user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Calling lambda function
si = calculate_si(p, r, t)

# Displaying the result
print("Simple Interest is:", si)