# Docstring
# The first string after the function is called the Document string or Docstring in short.
#  This is used to describe the functionality of the function.
#  The use of docstring in functions is optional but it is considered a good practice.

# syntax : print(function_name.__doc__)


def evenOdd(x):
    """Function to check if the number is even or odd"""
    
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")


print(evenOdd.__doc__)