# Program to find the greatest digit in a given number

# Taking input from the user
num = input("Enter a number: ")

# Initialize a variable to store the greatest digit
greatest = 0

# Loop through each digit in the number
for digit in num:
    
    # Convert the character digit into integer
    d = int(digit)
    
    # Check if the current digit is greater than the stored greatest digit
    if d > greatest:
        greatest = d   # Update the greatest digit

# Display the result
print("The greatest digit in the number is:", greatest)