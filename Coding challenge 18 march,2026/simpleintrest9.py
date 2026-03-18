# Program to calculate Simple Interest
# This version uses property (getter method) inside a class

# Creating a class
class Interest:
    
    # Constructor
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t
    
    # Property to calculate simple interest
    @property
    def simple_interest(self):
        return (self.p * self.r * self.t) / 100


# Taking input from user
p = float(input("Enter Principal (P): "))
r = float(input("Enter Rate (R): "))
t = float(input("Enter Time (T): "))

# Creating object
obj = Interest(p, r, t)

# Accessing property like variable
print("Simple Interest is:", obj.simple_interest)