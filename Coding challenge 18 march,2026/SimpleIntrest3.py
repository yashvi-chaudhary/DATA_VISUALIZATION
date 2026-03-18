# Check simple interest 

def SI(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest:", SI(p, r, t))