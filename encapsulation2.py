class Student:
    def __init__(self, name="Mark", marks=108):
        self.__name = name
        self.__marks = marks
    def studentdata(self):
         print("Name: {} marks: {}".format(self.__name, self.__marks))

s1=Student()
s2=Student("Vicky",209)

s1.studentdata()
s2.studentdata()

print("Name: {} marks: {}".format(s1.__name,s1.__marks))
print("Name: {} marks: {}".format(s2.__name, s2.__marks))

# An error coming from the above program can be fixed through name mangling.