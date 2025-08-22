from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started with a key")

    def stop(self):
        print("Car stopped with a brake")

class Bike(Vehicle):
    def start(self):
        print("Bike started with a kick")

    def stop(self):
        print("Bike stopped with a hand brake")

# Usage
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
    v.stop()
