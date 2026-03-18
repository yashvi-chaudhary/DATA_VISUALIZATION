# Program to check vote eligibility
# This version uses match-case (Python 3.10+) for decision making

# Taking input from the user
age = int(input("Enter your age: "))

# Using match-case with condition result
match age >= 18:
    case True:
        print("Eligible to vote")
    case False:
        print("Not Eligible to vote")