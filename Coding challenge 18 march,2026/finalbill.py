# Program to calculate final bill after discount
# This version uses a slightly different logic

# Taking input from the user
price = float(input("Enter the price of the product: "))
discount = float(input("Enter discount percentage: "))

# Calculating final price directly using formula
final_price = price * (100 - discount) / 100

# Displaying the result
print("Final price after discount:", final_price)