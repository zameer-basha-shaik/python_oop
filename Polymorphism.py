#Polymorphism

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting....")

    def stop(self):
        print("Vehicle has stopped....")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def start(self):
        print("Car is starting....")

    def stop(self):
        print("Car has stopped....")

class Bike(Vehicle):
    def __init__(self, brand, model, year, num_gears):
        super().__init__(brand, model, year)
        self.num_gears = num_gears

    def start(self):
        print("Bike is starting....")
    
    def stop(self):
        print("Bike has stopped....")
class Plane:
    pass

vehicles: list[Vehicle] = [
    Car("Honda", "CT", 2020, 4),
    Bike("Hero", "Delux", 2024, 4),
]

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()
