class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)  
print(dog1.species)

# Create a Person class
class Person:
    name="Sonu"

    # Create a constructor
    def __init__(self,age,address):
        self.age=age
        self.address=address
        pass

    # create a method for print details
    def details_person(self):
        print(f"The age of person: {self.age} And The Address of the Person:{self.address}")

# create a object for the person class
myPerson=Person(25,"Gurgaon")
myPerson.details_person()