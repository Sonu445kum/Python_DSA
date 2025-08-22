class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age!")

# Usage
s = Student("John", 20)
print(s.age)    # Calls getter
s.age = 25      # Calls setter
print(s.age)
s.age = -5      # Invalid
