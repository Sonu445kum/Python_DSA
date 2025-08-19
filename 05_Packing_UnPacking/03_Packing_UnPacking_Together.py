# We can use Packing and Unpacking in same function.

def together(*args, **kwargs):
    print("Positional:", args)
    print("Keyword arguments:", kwargs)

together(1, 2, 3, name="geeks for geeks", age=30)