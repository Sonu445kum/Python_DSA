# Generator in Python:
# A Generator in Python is a special type of function that allows you to 
# generate values one at a time instead of returning them all at once.

# it is created using the yield keyword.

# Normal function → returns a value (using return) and ends execution.
# Generator function → yields a value (using yield) but remembers its state and
# can resume where it left off.

# Why use Generators:
# Memory Efficient → They don’t store all values in memory, they generate values on the fly.

# Lazy Evaluation → They produce values only when needed.

# Infinite Sequences → Useful for infinite or very large data streams.

# Normal Function vs Generator


# Normal function
def get_numbers_list(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

print(get_numbers_list(5))   # [0, 1, 2, 3, 4]

# Generator function
def get_numbers_gen(n):
    for i in range(n):
        yield i

gen = get_numbers_gen(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2



print("New Line")
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)

# infinite Generator
def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = infinite_numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


# Generator Expressions (like list comprehension)
# List comprehension
nums = [x*x for x in range(5)]
print(nums)   # [0, 1, 4, 9, 16]

# Generator expression
gen = (x*x for x in range(5))
print(gen)    # <generator object ...>
print(list(gen))  # [0, 1, 4, 9, 16]

