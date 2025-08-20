# integer number
n = int(input("Enter Your Number: "))
print("\nYour Number is:", n, "\n")

# String
name = input("Enter Your Message: ")
print("\nYour Message:", name, "\n")

# Floating Number
price = float(input("Enter Your Price Rate: "))
print("\nYour Price is:", price, "\n")
print("Python")


import sys
for line in sys.stdin:
    print("You entered:", line.strip())
