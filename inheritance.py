#Parent/Super/Base class
class Animal:
    def speak(self):
        print("Animal is speaking")

#Child/Sub class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a=Animal()
d=Dog()
d.speak()

class Fruit:
    def __init__(self,fname, ftype):
        self.fruitname=fname
        self.fruittype=ftype

    def printname(self):
            print(self.fruitname,self.fruittype)

x=Fruit("apple","simple")
x.printname()

class Person:
    def __init__(self,fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

x=Person("John","Cena")
x.printname()

class Student(Person):
    pass
x=Student("Mike","Pompeo")
x.printname()

class Student(Person):
    def __init__(self,fname,lname):
        #self.firstname=fname
        #self.lastname=lname
        Person.__init__(self, fname, lname)
        def printname(self):
            print(self.firstname, self.lastname)
y=Student("Gloria","Muliro")
y.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname, self.lastname, "to the graduation, class of", self.graduationyear)

x=Student("Mike","Pompeo",2019)
print(x.graduationyear)
x.welcome()