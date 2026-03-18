# Program to print even numbers between 1 and N
# This version uses list comprehension (different logic)

# Taking input from the user
N = int(input("Enter the value of N: "))

# Using list comprehension to generate even numbers
even_numbers = [num for num in range(1, N + 1) if num % 2 == 0]

# Displaying the result
print("Even numbers between 1 and", N, "are:")
print(even_numbers)