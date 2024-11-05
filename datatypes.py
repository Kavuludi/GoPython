

number=67 #This is an integer.
second=45.98 #This is a float.
greeting="Hello World!" #This is a string
IsPythonInteresting= True #This is a boolean.

#Data structures
#Multiple values stored in a single variable.
cars=["Toyota","Mercedes", "Nissan", "BMW"] #This is a list. Values are ordered and changeable(mutable)
fruits=("banana", "orange", "mango")#This is a tuple. Values are ordered and non-changeable.
countries={"Kenya", "Tunisia", "Algeria"} #This is a set. Elements are unordered and non-changeable.
student={
    "firstname":"Peter",
    "age":25,
    "course": "Web Development"
} #This is a dictionary- Key-value pair.

#Determining the datatype

print(type(countries))
print(type(student))

#Typecasting-converting from one datatype to another.
print(float(number))
print(int(second))

print(number)
print(second)
print(greeting)
print(IsPythonInteresting)

print(countries)
print(fruits)
print(cars)
print(student)
print(student["course"])
