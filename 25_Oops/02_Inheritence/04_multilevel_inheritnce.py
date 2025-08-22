class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)   # call parent constructor
        self.model = model

    def info(self):
        print(f"Car: {self.brand}, Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def info(self):
        print(f"Electric Car: {self.brand}, Model: {self.model}, Battery: {self.battery} kWh")

# Usage
e = ElectricCar("Tesla", "Model S", 100)
e.info()  # Electric Car: Tesla, Model: Model S, Battery: 100 kWh
