# Program to print even numbers between 1 and N
# This version uses recursion (different logic)

# Recursive function to print even numbers
def print_even(n):
    
    # Base condition
    if n == 0:
        return
    
    # Recursive call
    print_even(n - 1)
    
    # Print only if number is even
    if n % 2 == 0:
        print(n, end=" ")


# Taking input from user
N = int(input("Enter the value of N: "))

print("Even numbers between 1 and", N, "are:")

# Calling recursive function
print_even(N)