# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving "

class Plane(Vehicle):
    def move(self):
        return "Flying "

class Boat(Vehicle):
    def move(self):
        return "Sailing "

# Test Polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
