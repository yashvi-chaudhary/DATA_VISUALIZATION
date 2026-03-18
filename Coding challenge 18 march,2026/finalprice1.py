# Program to calculate final price after discount
# This version uses input validation and separate function for discount calculation

# Function to compute discount amount
def get_discount_amount(price, discount):
    return (price * discount) / 100


# Taking input from user
price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

# Checking for valid input
if discount < 0 or discount > 100:
    print("Invalid discount percentage!")
else:
    # Calling function
    discount_amount = get_discount_amount(price, discount)
    
    # Calculating final price
    final_price = price - discount_amount
    
    # Displaying result
    print("Final price after discount is:", final_price)