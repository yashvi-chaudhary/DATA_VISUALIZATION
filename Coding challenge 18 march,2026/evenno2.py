# Program to print even numbers between 1 and N
# This version uses step value in range()

# Taking input from user
N = int(input("Enter the value of N: "))

# Starting from 2 and jumping by 2
for i in range(2, N + 1, 2):
    print(i, end=" ")