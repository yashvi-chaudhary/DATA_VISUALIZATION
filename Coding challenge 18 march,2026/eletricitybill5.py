# Program to calculate electricity bill
# This version uses a loop to add bill for each unit (different logic)

# Taking input from the user
units = int(input("Enter units consumed: "))

bill = 0

# Loop through each unit and add cost
for i in range(1, units + 1):
    
    # Applying different rates based on unit number
    if i <= 100:
        bill += 5
    elif i <= 200:
        bill += 7
    else:
        bill += 10

# Displaying the result
print("Total electricity bill amount is:", bill)