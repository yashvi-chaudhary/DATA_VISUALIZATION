# Program to print even numbers between 1 and N
# This version uses map() with a helper function (different logic)

# Helper function to return number if even, else None
def check_even(num):
    if num % 2 == 0:
        return num
    return None

# Taking input from user
N = int(input("Enter the value of N: "))

# Creating list from 1 to N
numbers = list(range(1, N + 1))

# Using map() to process numbers
result = list(map(check_even, numbers))

# Removing None values
even_numbers = [x for x in result if x is not None]

# Displaying result
print("Even numbers between 1 and", N, "are:")
print(even_numbers)