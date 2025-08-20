# Base Exception
try:
    raise BaseException("This is a BaseException")
except BaseException as e:
    print(e)

# Exception
try:
    raise Exception("This is a generic exception")
except Exception as e:
    print(e)

# ArithmeticError
try:
    raise ArithmeticError("Arithmetic error occurred")
except ArithmeticError as e:
    print(e)

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(e)

# OverflowError
import math

try:
    result = math.exp(1000)  # Exponential function with a large argument
except OverflowError as e:
    print(e)

# FloatingPointError
# import sys
# import math

# sys.float_info.max = 1.79e+308  # Maximum float value

# try:
#     math.sqrt(-1.0)  # This doesn't raise a FloatingPointError by default
# except FloatingPointError as e:
#     print(e)

# AssertionError
try:
    assert 1 == 2, "Assertion failed"
except AssertionError as e:
    print(e)

# AttributeError
class MyClass:
    pass

obj = MyClass()

try:
    obj.some_attribute
except AttributeError as e:
    print(e)

# indexError
my_list = [1, 2, 3]

try:
    element = my_list[5]
except IndexError as e:
    print(e)

# KeyError
d = {"key1": "value1"}

try:
    val = d["key2"]
except KeyError as e:
    print(e)

# MemoryError
try:
    li = [1] * (10**10)
except MemoryError as e:
    print(e)

# NameError
# try:
#     print(var)
# except NameError as e:
#     print(e)

# OSError
try:
    open("non_existent_file.txt")
except OSError as e:
    print(e)
