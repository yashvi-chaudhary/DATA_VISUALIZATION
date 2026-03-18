# Program to check vote eligibility
# This version uses exception handling and loop for valid input

while True:
    try:
        # Taking input from user
        age = int(input("Enter your age: "))
        
        # Validation: age should not be negative
        if age < 0:
            print("Invalid age! Please enter a positive number.")
            continue
        
        # Valid input received → exit loop
        break
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Checking eligibility
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")