#In Python there is no provision to specify the type of access that a class member may have.
#Where the instance variables are initialized inside the class with no restriction on accessing the value of instance variable from outside the class.
class Student:
    def __init__(self, first_name="John", marks=99):
        self.first_name = first_name
        self.marks = marks

s1=Student()
s2=Student("Karanja",67)

print("Name: {} marks: {}".format(s1.first_name, s1.marks))
print("Name: {} marks: {}".format(s2.first_name, s2.marks))




