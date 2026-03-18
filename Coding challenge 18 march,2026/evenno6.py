# Program to print even numbers between 1 and N
# This version uses filter() function (different logic)

# Taking input from the user
N = int(input("Enter the value of N: "))

# Creating a list from 1 to N
numbers = list(range(1, N + 1))

# Using filter with lambda to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Displaying the result
print("Even numbers between 1 and", N, "are:")
print(even_numbers)