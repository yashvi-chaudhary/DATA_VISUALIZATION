# Program to find the factorial of a number

# Taking input from the user
num = int(input("Enter a number: "))

# Initialize factorial variable with 1
factorial = 1

# Check if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers")

# If number is 0, factorial is 1
elif num == 0:
    print("The factorial of 0 is 1")

# Calculate factorial using a loop
else:
    for i in range(1, num + 1):
        factorial = factorial * i   # Multiply numbers from 1 to num

    # Display the result
    print("The factorial of", num, "is", factorial)