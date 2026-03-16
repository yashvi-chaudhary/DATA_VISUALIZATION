# Program to display even factors of a given number

# Taking input from the user
num = int(input("Enter a number: "))

print("Even factors of", num, "are:")

# Loop from 1 to the given number
for i in range(1, num + 1):
    
    # Check if i is a factor of the number
    if num % i == 0:
        
        # Check if the factor is even
        if i % 2 == 0:
            print(i)   # Print the even factor