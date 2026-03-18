#Program to check whether a person is eligible to vote
# This version uses a different logic than the previous one

# Taking age as input from the user
age = int(input("Enter your age: "))

# Using reversed condition logic
if age < 18:
    print("Not Eligible to vote")
else:
    print("Eligible to vote")