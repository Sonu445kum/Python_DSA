# Functools:
# functools is a Python standard library module.

# It provides higher-order functions: functions that act on or return other functions.

# Useful for function manipulation, caching, partial application, decorators, etc.

# Summarry:
# reduce() → cumulative operations on iterables.

# partial() → fix arguments to create new functions.

# lru_cache() → memoization/caching for performance.

# cmp_to_key() → custom sorting.

# wraps() → preserve metadata in decorators.

from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 120

# Partials
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)   # always raises to power 2
cube = partial(power, exp=3)     # always raises to power 3

print(square(5))  # 25
print(cube(2))    # 8

# lru_cache()
from functools import lru_cache

@lru_cache(maxsize=None)  # unlimited cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55
print(fib(50))  # Fast because of caching


# cmp_to_key()
# Convert an old-style comparison function to a key function (for sorting)
from functools import cmp_to_key

# Custom comparator: sort numbers by their last digit
def compare(x, y):
    return (x % 10) - (y % 10)

nums = [23, 45, 12, 89, 34]
sorted_nums = sorted(nums, key=cmp_to_key(compare))
print(sorted_nums)  # [12, 23, 34, 45, 89]


# wraps()

# Helps when writing decorators → keeps the original function’s name & docstring.
from functools import wraps

def decorator(func):
    @wraps(func)   # keeps function metadata
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator
def greet(name):
    """This function greets the user"""
    print("Hello", name)

greet("Sonu")
print(greet.__name__)   # greet (not wrapper)
print(greet.__doc__)    # "This function greets the user"

