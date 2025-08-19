# UnPacking Arguments
# Unpacking allows values from an iterable (list, tuple, or dictionary) 
# to be passed as separate arguments to a function.


# 1. Unpacking a List/Tuple with *
#  We use * to unpack elements from a list/tuple.


def addition(a, b, c):
    return a + b + c

num = (1, 5, 10)  
result = addition(*num) 
print("Sum:", result)


# 2. Unpacking a Dictionary with **
# We use ** to unpack key-value pairs from a dictionary.

def info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

data = {"name": "geeks for geeks", "age": 30, "country": "India"}
info(**data)