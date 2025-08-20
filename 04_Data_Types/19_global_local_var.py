
# Local Variables
def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()


print("New Line..!!")

# Global Variables
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)