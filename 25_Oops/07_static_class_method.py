# Static Methods and Class Methods

# Static Method: A method that does not require access to instance or class.
#  It’s defined using @staticmethod decorator.

# Class Method: A method that receives the class as its first argument (cls).
#  It’s defined using @classmethod decorator.


class Dog:
    @staticmethod
    def info():
        print("Dogs are loyal animals.")

    @classmethod
    def count(cls):
        print("There are many dogs of class", cls)

dog = Dog()
dog.info()  # Static method call
dog.count()  # Class method call