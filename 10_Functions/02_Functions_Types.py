# def function_name(parameter: data_type) -> return_type:
#     """Docstring"""
#     # body of the function
#     return expression

# data_type and return_type are optional in function declaration,
#  meaning the same function can also be written as:

#  def function_name(parameter) :
#     """Docstring"""
#     # body of the function
#     return expression


def evenOdd(x: int) ->str:
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
print()

# Functions with no return types

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))



# Types of Python Function Arguments
# Python supports various types of arguments that can be passed at the time of the function
#  call. In Python, we have the following function argument types in Python:

# Default argument
print("Default Arguments")
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


myFun(10)

# Keyword arguments (named arguments)
print()
print("Keywords Arguments:")
def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# Positional arguments
print()
print("Position Arguments:")
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)


print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

# Arbitrary arguments (variable-length arguments *args and **kwargs)
print()
print("Arbitary Arguments")
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


myFun(first='Geeks', mid='for', last='Geeks')