# Program to calculate Simple Interest using a function
# This version prints the result inside the function

# Defining the function
def calculate_si(principal, rate, time):
    
    # Calculating simple interest
    si = (principal * rate * time) / 100
    
    # Printing the result inside the function
    print("Simple Interest is:", si)


# Taking input from the user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Calling the function
calculate_si(p, r, t)