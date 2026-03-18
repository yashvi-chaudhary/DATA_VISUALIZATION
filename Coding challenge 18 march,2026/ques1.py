# Program to calculate the final bill after discount

# Taking input from the user for the price of the product
price = float(input("Enter the price of the product: "))

# Taking input for the discount percentage
discount = float(input("Enter the discount percentage: "))

# Calculating the discount amount
discount_amount = (price * discount) / 100

# Calculating the final price after discount
final_price = price - discount_amount

# Displaying the final price
print("Final price after discount is:", final_price)