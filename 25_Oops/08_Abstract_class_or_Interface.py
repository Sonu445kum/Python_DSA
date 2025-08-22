# Abstract Classes and Interfaces

# Abstract classes provide a template for other classes. 
# These classes can't be instantiated directly.
# They contain abstract methods, which are methods that must be implemented by subclasses

# Abstract classes are defined using abc module in Python. 
# Let’s see an example of using an abstract class to define a required method for subclasses:

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof")

dog = Dog()
dog.sound()