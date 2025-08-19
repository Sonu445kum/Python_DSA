# List:
# In Python, a list is a built-in dynamic sized array (automatically grows and shrinks).
#  We can store all types of items (including another list) in a list.

# Can contain duplicate items.
# Mutable : We can modify, replace or delete the items.
# Ordered : Maintains the order of elements based on how they are added.
# Items can be accessed directly using their position (index), starting from 0.
# May contain mixed type of items, this is possible because a list mainly stores 
# references at contiguous locations and actual items maybe stored at different locations

# Creating a Python list with different data types
a = [10, 20, "GfG", 40, True]
print(a)

# Accessing elements using indexing
print(a[0])  # 10
print(a[1])  # 20
print(a[2])  # "GfG"
print(a[3])  # 40
print(a[4])  # True

# Checking types of elements
print(type(a[2]))  # str
print(type(a[4]))  # bool


# **Notes:Lists Store References, Not Values
# Each element in a list is not stored directly inside the list structure.
#  Instead, the list stores references (pointers) to the actual objects in memory.
#  Example (from the image represent.


# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

# Using List Constructor
# we can also create a list by passing an iterable (like a string, tuple or another list)
#  to list() function.

# From a tuple
a = list((1, 2, 3, 'apple', 4.5))  
print(a)


# Creating List with Repeated Elements
# We can create a list with repeated elements using the multiplication operator.

# Create a list [2, 2, 2, 2, 2]
a = [2] * 5

# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7

print(a)
print(b)

# Adding Elements into List
# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.

# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a)


# Removing Element from the List
# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)


# Iterating Overs the List
a = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in a:
    print(item)


# Nested Lists in Python
# A nested list is a list within another list, which is useful for 
# representing matrices or tables. We can access nested elements by chaining indexes.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 2, column 3
print(matrix[1][2])

# List Comprehension in Python
# List comprehension is a concise way to create lists using a single line of code.
#  It is useful for applying an operation or filter to items in an iterable, 
# such as a list or range.


# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)