# Program to check vote eligibility
# This version uses a dictionary to map result

# Taking input from the user
age = int(input("Enter your age: "))

# Creating dictionary for result mapping
status = {
    True: "Eligible to vote",
    False: "Not Eligible to vote"
}

# Evaluating condition and fetching result
result = status[age >= 18]

# Displaying result
print(result)