# Create a class and Apply the __str__ () method
# li =[1,2,3,4,5]
# res=(val*2 for val in li)
# print(type(res))

# __str__() Method:
# __str__ method in Python allows us to define a custom string representation of an object.
#  By default, when we print an object or convert it to a string using str(),
#  Python uses the default implementation, which returns a string like <__main__.ClassName object at 0x00000123>.


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1)  
print(dog2)