# There are three way to take input from the user in the python
# 1-> input() Method
# 2 -> sys.stdin
# 3 - > fileInput.Input


# Use input() → for interactive user input.
# Use sys.stdin.readline() → for faster input in large data.
# Use sys.stdin.read() → to read everything at once


# Take single input
name = input("Enter your name: ")
print("Hello,", name)


# Take multiple values
a, b = input("Enter two numbers: ").split()
print("a =", a, "b =", b)


a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)

