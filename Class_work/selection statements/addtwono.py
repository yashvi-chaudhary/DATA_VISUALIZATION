# Program to add two numbers using a function

# Function definition to add two numbers
def add_numbers(num1, num2):
    # Add the two numbers
    result = num1 + num2
    
    # Return the result
    return result


# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Calling the function and storing the result
sum_result = add_numbers(a, b)

# Displaying the result
print("The sum of the two numbers is:", sum_result)