# Python does not support method overloading in the same way as Java or C++ 
# (where you can define multiple methods with the same name but different parameters).

# But, in Python we can achieve similar behavior using:

# Default arguments

# Variable-length arguments (*args, **kwargs)

# Single method handling multiple cases




# Using the default arguments
print("Using the Default:")
class Math:
    def add(self, a=0, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(5, 10))     # 15
print(m.add(5, 10, 20)) # 35
print(m.add(5))         # 5

print("*args")
# Using *args (Flexible Parameters)
class Math:
    def add(self, *args):
        return sum(args)

m = Math()
print(m.add(2, 3))            # 5
print(m.add(1, 2, 3, 4, 5))   # 15

print("Single Method Handling:")
# Single method handling multiple cases
class Demo:
    def show(self, x):
        print("One argument:", x)

    def show(self, x, y):   # This overrides the previous one
        print("Two arguments:", x, y)

d = Demo()
d.show(10, 20)   # Works
# d.show(10)     # ❌ Error: missing 1 required positional argument



