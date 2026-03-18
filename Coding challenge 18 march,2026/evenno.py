# Program to print all even numbers between 1 and N

# Taking input from the user
N = int(input("Enter the value of N: "))

# Printing even numbers between 1 and N
print("Even numbers between 1 and", N, "are:")

# Using a loop to check numbers
for i in range(1, N + 1):
    
    # Checking if the number is even
    if i % 2 == 0:
        print(i, end=" ")