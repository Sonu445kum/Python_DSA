# In Python, Operator Overloading means giving special meaning to operators (+, -, *, <, etc.)

#  when they are used with user-defined objects (classes).

# __add__(self, other) → for +

# __sub__(self, other) → for -

# __mul__(self, other) → for *

# __truediv__(self, other) → for /

# __lt__(self, other) → for <

# __eq__(self, other) → for ==

# __str__(self) → for print()

# Overloading + Operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)   # (6, 8)


# Overloading * operator
class Vector:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Vector(self.value * other.value)

    def __str__(self):
        return f"Vector({self.value})"

v1 = Vector(3)
v2 = Vector(4)
print(v1 * v2)   # Vector(12)

# Overloading Comparison Operators
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):   # greater than >
        return self.marks > other.marks

    def __eq__(self, other):   # equal to ==
        return self.marks == other.marks

s1 = Student(85)
s2 = Student(90)
s3 = Student(85)

print(s1 > s2)   # False
print(s1 == s3)  # True

