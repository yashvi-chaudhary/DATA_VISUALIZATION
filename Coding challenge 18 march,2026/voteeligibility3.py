# Program to check vote eligibility
# This version uses a function and returns True/False

# Function to check eligibility
def is_eligible(age):
    
    # Return True if age is 18 or above, otherwise False
    return age >= 18


# Taking input from user
age = int(input("Enter your age: "))

# Calling function and storing result
result = is_eligible(age)

# Checking result and printing message
if result:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")