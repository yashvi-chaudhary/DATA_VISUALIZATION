# Program to calculate the final price after applying discount

# Taking input from the user
price = float(input("Enter the price of the product: "))
discount = float(input("Enter the discount percentage: "))

# Calculating the discount amount
discount_amount = (price * discount) / 100

# Calculating the final price after discount
final_price = price - discount_amount

# Displaying the final price
print("Final price after discount is:", final_price)