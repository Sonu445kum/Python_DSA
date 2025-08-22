class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Marks:
    def __init__(self, marks):
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)

# Child class inheriting from both
class Student(Person, Marks):
    def __init__(self, name, marks):
        Person.__init__(self, name)
        Marks.__init__(self, marks)

# Usage
s = Student("John", 95)
s.display()       # Name: John
s.show_marks()    # Marks: 95
