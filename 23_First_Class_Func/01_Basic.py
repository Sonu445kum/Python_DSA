# First Class functions in Python:
# First-class function is a concept where functions are treated as first-class citizens.
#  By treating functions as first-class citizens, Python allows you to write more abstract,
#  reusable, and modular code. This means that functions in such languages are treated like
#  any other variable. They can be passed as arguments to other functions, returned as values
#  from other functions, assigned to variables and stored in data structures.

# Characteristics of First-Class Functions:
# Assigned to Variables: We can assign functions to variables.


def msg(name):
    return f"Hello, {name}!"

# Assigning the function to a variable
f = msg

# Calling the function using the variable
print(f("Anurag"))



# Passed as Arguments: We can pass functions as arguments to other functions.
def msg(name):
    return f"Hello, {name}!"

def fun1(fun2, name):
    return fun2(name)

# Passing the greet function as an argument
print(fun1(msg, "Bob"))



# Returned from Functions: Functions can return other functions.
def fun1(msg):
    def fun2():
        return f"Message: {msg}"
    return fun2

# Getting the inner function
func = fun1("Hello, World!")
print(func())

# Stored in Data Structures: Functions can be stored in data structures
#  such as lists, dictionaries, etc.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))       
print(d["subtract"](5, 3))


