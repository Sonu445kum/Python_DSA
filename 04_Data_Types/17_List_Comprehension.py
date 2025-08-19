# List Comprehension
# List comprehension is a way to create lists using a concise syntax.
#  It allows us to generate a new list by applying an expression to each item in 
# an existing iterable (such as a list or range). 
# This helps us to write cleaner, more readable code compared to traditional looping techniques.


# Syntax of List Comprehension
# [expression for item in iterable if condition]


a = [2,3,4,5]

res = [val ** 2 for val in a]

print(res)

# For Loops Vs List Comprehension
a = [1, 2, 3, 4, 5]

# Create an empty list 'res' to store results
res = []
# Iterate over each element in list 'a'
for val in a:
    # Multiply each element by 2 and append it to 'res'
    res.append(val * 2)

print(res)

# List Comprehension in the Conditional Statements
a = [1, 2, 3, 4, 5]

res = [val * 2 for val in a]

print(res)

a = [1, 2, 3, 4, 5]

res = [val for val in a if val % 2 == 0]

print(res)


# Creates a list of numbers from 0 to 9
a = [i for i in range(10)]

print(a)

# Using Nested Loops
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]

print(coordinates)


# Flattening a list of lists
# Suppose we have a list of lists and we want to convert it into a single list.
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [val for row in mat for val in row]

print(res)