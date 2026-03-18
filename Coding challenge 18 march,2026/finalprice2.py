# Program to calculate final price after discount
# This version uses try-except for safe input handling

try:
    # Taking input from user
    price = float(input("Enter the price: "))
    discount = float(input("Enter discount percentage: "))
    
    # Checking valid discount range
    if discount < 0 or discount > 100:
        print("Invalid discount percentage!")
    else:
        # Calculating final price
        final_price = price - (price * discount / 100)
        
        # Displaying result
        print("Final price after discount is:", final_price)

except ValueError:
    print("Invalid input! Please enter numeric values.")