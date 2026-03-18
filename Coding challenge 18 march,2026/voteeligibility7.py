# Program to check vote eligibility
# This version uses a loop with multiple inputs and stores results in a list

# Creating a list to store results
results = []

# Asking how many persons to check
n = int(input("Enter number of persons: "))

# Loop to take multiple inputs
for i in range(n):
    
    age = int(input(f"Enter age of person {i+1}: "))
    
    # Checking eligibility
    if age >= 18:
        results.append("Eligible")
    else:
        results.append("Not Eligible")

# Displaying all results
print("Voting Eligibility Results:")
for res in results:
    print(res)