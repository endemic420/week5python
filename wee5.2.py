# Define a base class Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Car class with move() implementation
class Car(Vehicle):
    def move(self):
        print("Driving")
        
# Plane class with move() implementation
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Define a base class Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Dog class with move() implementation
class Dog(Animal):
    def move(self):
        print("Running")

# Fish class with move() implementation
class Fish(Animal):
    def move(self):
        print("Swimming")

# Bird class with move() implementation
class Bird(Animal):
    def move(self):
        print("Flying")

# Demonstrate the polymorphic behavior
def main():
    vehicles = [Car(), Plane()]
    animals = [Dog(), Fish(), Bird()]

    print("Vehicles moving:")
    for v in vehicles:
        v.move()

    print("\nAnimals moving:")
    for a in animals:
        a.move()

if __name__ == "__main__":
    main()
