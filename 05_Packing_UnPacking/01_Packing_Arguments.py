# Packing Arguments
# Packing allows multiple values to be combined into 
# a single parameter using * (for tuples/lists) and ** (for dictionaries).

# *args (Non-keyword arguments): Packs multiple positional arguments into a tuple.
#  **kwargs (Keyword arguments): Packs multiple keyword arguments into a dictionary.

# 1 => Packing With *args
# The * operator allows us to pass multiple arguments to a
#  function and pack them into a tuple.

def sample(*args):
    print("Packed arguments:", args)

sample(1, 2, 3, 4, "geeks for geeks")


# 2 =>Packing with **kwargs
#  ** operator is used to collect multiple keyword arguments into a dictionary.

def sample(**kwargs):
    print("Packed keyword arguments:", kwargs)

sample(name="Anaya", age=25, country="India")