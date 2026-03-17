# Program to check whether a number is Even or Odd using a function

# Function definition
def check_even_odd(num):
    # Check if the number is divisible by 2
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

# Taking input from the user
number = int(input("Enter a number: "))

# Calling the function and passing the number
check_even_odd(number)