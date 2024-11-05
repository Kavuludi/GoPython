#A program to allow a user enter three numbers, check and return the largest

first=int(input("Enter first number: "))
second=int(input("Enter second number: "))
third=int(input("Enter third number: "))

if first>second and first>third:
    print(first, "is the greatest number")
elif second>first and second>third:
    print(second, "is the greatest number")
else:
    print(third, "is the greatest number")
