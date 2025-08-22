class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):   # Overriding method
        print(f"{self.name} barks!")

# Usage
d = Dog("Tommy")
d.speak()   # Tommy barks!
