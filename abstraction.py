from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("Tesla mileage is 30kmph")

class Suzuki(Car):
    def mileage(self):
        print("Suzuki mileage is 25kmph")

class Duster(Car):
    def mileage(self):
        print("Dust mileage is 50kmph")

class Renault(Car):
    def mileage(self):
        print("Renault mileage is 27kmph")

t=Tesla()
t.mileage()

r=Renault()
r.mileage()

s=Suzuki()
s.mileage()

d=Duster()
d.mileage()

class Polygon(ABC):
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

class Hexagon(Polygon):
    def sides(self):
        print("Hexagon has 6 sides")

class Square(Polygon):
    def sides(self):
        print("Sqaure has 4 sides")

x=Triangle()
x.sides()

q=Square()
q.sides()

p=Pentagon()
p.sides()

h=Hexagon()
h.sides()
