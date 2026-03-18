# Program to calculate final price after discount
# This version uses a loop to allow multiple calculations

while True:
    
    # Taking input from user
    price = float(input("Enter the price: "))
    discount = float(input("Enter discount percentage: "))
    
    # Calculating final price
    final_price = price - (price * discount / 100)
    
    # Displaying result
    print("Final price after discount is:", final_price)
    
    # Asking user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ")
    
    if choice.lower() != "yes":
        break