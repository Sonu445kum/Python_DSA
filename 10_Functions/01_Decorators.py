# without Arguments
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")
greet()

print()
print("Lines ends here..!!")

# with arguments
def decorator_name(func):
    def wrapper(*args,**kwargs):
        print("Before Calling The Functions:")
        result = func(*args,**kwargs)
        print("After the calling the functions:")
        return result
    
    return wrapper

@decorator_name
def add(a,b):
    return a+b
print(add(2,4))
