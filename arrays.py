
courses=["MIT","Datascience","Cyber Security"]
print(courses)

#Accessing an element in an array.
print(courses[0])
print(courses[1])
print(courses[2])

#Looping through an array.
for y in courses:
    print("The best course is",y)

#Adding a new element
courses.append("Android Development")
print(courses)
for y in courses:
    print("The best course is",y)

#Deleting an element in an array
courses.remove("MIT")
print(courses)
for y in courses:
    print("The best course is",y)