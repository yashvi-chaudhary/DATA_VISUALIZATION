# Program to print even numbers between 1 and N
# This version uses generator function (different logic)

# Generator function to yield even numbers
def generate_even(n):
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i   # Yield even number one by one


# Taking input from user
N = int(input("Enter the value of N: "))

print("Even numbers between 1 and", N, "are:")

# Using generator
for num in generate_even(N):
    print(num, end=" ")