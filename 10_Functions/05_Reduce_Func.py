# Reduce() Function
# The reduce() function in Python applies a given function cumulatively to all items in an iterable,
#  reducing it to a single final value.

# Syntax:from functools import reduce
# reduce(function, iterable[, initializer])

# function: A function that takes two arguments and returns a single value.
# iterable: The sequence to be reduced (list, tuple, etc.).
# initializer (optional): A starting value that is placed before first element

# Example:

from functools import reduce
# create a functions
def addNum(x,y):
    return x+y
num =[1,2,3,4,5]
result =reduce(addNum,num)
print(result)


# Also We can solve above problems with the lambda
from functools import reduce
def add(x,y):
    return x+y

num =[10,20,30,30,40]
res = reduce(lambda x,y:x+y,num)
print(res)

# Using reduce() with operator Module
import functools
import operator

a = [1, 3, 5, 6, 2]

print(functools.reduce(operator.add, a)) # Sum of list
print(functools.reduce(operator.mul, a)) # Product of list
print(functools.reduce(operator.add, ["geeks", "for", "geeks"])) # String concatenation
print("New List:",a)

# using initilizer
from functools import reduce
nums =[1,2,3]

# using reduce functions here
initilizerResult =reduce(lambda x,y:x+y,nums,10)
print(initilizerResult)

# how to works of the above problems
# Step 1: x=10, y=1 → 10+1 = 11
# Step 2: x=11, y=2 → 11+2 = 13
# Step 3: x=13, y=3 → 13+3 = 16

# Difference Between reduce() and accumulate()
# The accumulate() function (from itertools) and reduce() (from functools) both apply a function cumulatively to 
#  items in a sequence. However, accumulate() returns an iterator of intermediate results, 
# while reduce() returns only final value.

from itertools import accumulate
from operator import add
number =[1,2,3,4,5]
result = accumulate(number,add)
print(list(result))

