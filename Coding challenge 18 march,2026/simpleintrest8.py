# Program to calculate Simple Interest
# This version uses class (OOP concept) instead of simple function

# Creating a class
class SimpleInterest:
    
    # Constructor to initialize values
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t
    
    # Method to calculate SI
    def calculate(self):
        return (self.p * self.r * self.t) / 100


# Taking input from user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Creating object of class
obj = SimpleInterest(p, r, t)

# Calling method
result = obj.calculate()

# Displaying result
print("Simple Interest is:", result)