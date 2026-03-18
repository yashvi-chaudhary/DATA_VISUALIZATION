# Program to calculate final bill after discount
# This version uses a function and updates the price variable directly

# Function to calculate final price
def calculate_final_price(price, discount):
    
    # Reduce price directly by discount percentage
    price -= (price * discount / 100)
    
    return price


# Taking input from user
price = float(input("Enter the price: "))
discount = float(input("Enter discount percentage: "))

# Calling the function
final_amount = calculate_final_price(price, discount)

# Displaying the result
print("Final price after discount is:", final_amount)