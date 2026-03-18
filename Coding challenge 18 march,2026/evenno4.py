# Program to print even numbers between 1 and N
# This version stores even numbers in a list first, then prints them

# Taking input from the user
N = int(input("Enter the value of N: "))

# Creating an empty list to store even numbers
even_list = []

# Loop through numbers from 1 to N
for i in range(1, N + 1):
    
    # Check if number is even
    if i % 2 == 0:
        even_list.append(i)   # Add even number to list

# Printing the list of even numbers
print("Even numbers between 1 and", N, "are:")
print(even_list)