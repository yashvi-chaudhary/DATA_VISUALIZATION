# Check electricity bill after discount

units = int(input("Enter units consumed: "))

bill = 0

if units <= 50:
    bill = units * 4
elif units <= 150:
    bill = units * 6
else:
    bill = units * 8

print("Total bill amount:", bill)