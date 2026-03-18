# Program to check whether a person is eligible to vote

# Taking age as input from the user
age = int(input("Enter your age: "))

# Checking the eligibility condition
# In India, a person can vote if age is 18 or above
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")