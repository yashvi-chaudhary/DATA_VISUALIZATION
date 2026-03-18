# Program to calculate final price after discount

# Taking inputs
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

# Calculating discount value first
discount_value = price / 100 * discount

# Final price
final_price = price - discount_value

# Printing result
print("Final price after discount:", final_price)