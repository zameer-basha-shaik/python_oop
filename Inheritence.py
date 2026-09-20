# Inheritance
# Creating new classes (subclasses or derived classes) from existing classes, which inherits it's attributes
# and methods

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting....")

    def stop():
        print("Vehicle has stopped....")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_wheels, num_doors):
        super().__init__(brand, model, year)
        self.no_doors = num_doors
        self.no_wheels = num_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, type, num_gears):
        super().__init__(brand, model, year)
        self.type = type
        self.num_gears = num_gears

car = Car("Kia", "Sonet", 2025, 4, 4)
bike = Bike("RE", "Standard", 2000, "Cruiser", 5)

print(car.__dict__)
car.start()
bike.start()
  