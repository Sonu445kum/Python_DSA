# Getter: Used to access value of an attribute.
# Setter: Used to modify value of an attribute.

class Dog:
    def __init__(self, name, age):
        self._name = name  # Conventionally private variable
        self._age = age  # Conventionally private variable

    @property
    def name(self):
        return self._name  # Getter

    @name.setter
    def name(self, value):
        self._name = value  # Setter

    @property
    def age(self):
        return self._age  # Getter

    @age.setter
    def age(self, value):
        if value < 0:
            print("Age cannot be negative!")
        else:
            self._age = value  # Setter
dog = Dog("Bruno", 5)

print(dog.name)  # Calls @property -> Bruno
print(dog.age)   # Calls @property -> 5

dog.name = "Rocky"   # Calls @name.setter
print(dog.name)      # Rocky

dog.age = -3         # Calls @age.setter -> "Age cannot be negative!"
print(dog.age)       # Still 5 (unchanged)

dog.age = 7
print(dog.age)       # 7
