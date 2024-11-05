#Strings
from variables import firstname

text= "Hello World!"
course="WEB DEVELOPMENT"

print(text)

#Accessing an element in a string
print(text[0])
print(text[6])

#Size/Length of a string
print(len(text))

#Modifying a string
print(course.lower())
print(text.upper())

#String concatenation-Joining two or more strings
greeting="Hello there!"
firstname="John"
lastname="Waka"

print(greeting + firstname + lastname)
print(greeting + " " + firstname + " " + lastname)
