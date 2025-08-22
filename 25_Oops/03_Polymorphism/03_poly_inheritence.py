class Vehicle:
    def move(self):
        print("Vehicles can move")

class Car(Vehicle):
    def move(self):
        print("Car drives on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat sails on water")

# Usage
v = Vehicle()
c = Car()
b = Boat()

for obj in (v, c, b):
    obj.move()
