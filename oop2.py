#The __int__()Function-used to assign values to object properties, or other operations that re necessary to do when object is being created.
class person:
    def __init__(self, name, age, gender):
        self.name =name
        self.age = age
        self.gender = gender

person1=person("Peter","24","Male")
print(person1.name)

person2=person("Joan","20","Female")
print(person2.name)

person3=person("Rose","56","Female")
print(person3.name)

#__str__() Function

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

car1=car("Mercedes","Benz EQB","2004")
car2=car("'Toyota","Fortuner","2015")
car3=car("BMW","BMW M760i XDrive","2010")
car4=car("Subaru","Imprezza","2018")

print(car1)

#Methods
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def myfunc(self):
        print("Hello everyone, my name is "+self.name,"\n","I am",self.age,"years old.")

p1=Person("Peter","24","Male")
p1.myfunc()