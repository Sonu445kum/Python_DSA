class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):  # Method overriding
        print("Woof")

dog = Dog()
dog.sound()