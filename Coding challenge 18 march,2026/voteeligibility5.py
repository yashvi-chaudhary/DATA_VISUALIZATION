# Program to check vote eligibility
# This version uses a function that returns a message string

# Function to check eligibility
def check_vote(age):
    
    # Using if-else inside function and returning message
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not Eligible to vote"


# Taking input from user
age = int(input("Enter your age: "))

# Calling function and printing result directly
print(check_vote(age))