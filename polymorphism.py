#Same method across all classes but different implementation.
class Rectangle:
    def shape(self):
        print("Drawing a rectangle")

class Rhombus:
    def shape(self):
        print("Drawing a rhombus")

class Parallelogram:
    def shape(self):
        print("Drawing a parallelogram")

r=Rectangle()
r.shape()

rhom=Rhombus()
rhom.shape()

p=Parallelogram()
p.shape()

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        def move(self):
            print("Move!")

class Car(Vehicle):

    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Fly!")

car1=Car("Ford","Mustang",2014)
boat1=Boat("Ibiza","Touring",1999)
plane1=Plane("Boeing","747",2000)

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()