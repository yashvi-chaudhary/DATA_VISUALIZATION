# Program to print even numbers between 1 and N
# This version uses a while loop instead of a for loop

# Taking input from the user
N = int(input("Enter the value of N: "))

print("Even numbers between 1 and", N, "are:")

# Starting number
i = 1

# Using while loop
while i <= N:
    
    # Checking if number is even
    if i % 2 == 0:
        print(i, end=" ")
    
    i += 1