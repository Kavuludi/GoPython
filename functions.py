#Built-in functions

y=max(34, 56, 70, 18)
print("The maximum number is",y)

x=min(40, 56, 14, 90)
print("The minimum number is",x)

z=pow(2,3)
print("The power of 2 is",z)

#User-defined functions
def greeting():
    print("Hello World!")
#Calling a function
greeting()

def multiply():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("The multiplication is",a*b)
multiply()

#Parameters/Variable and arguments/Values
def add(c,d):
    print("The addition is",c+d)
add(4,5)
add(60,70)
add(50,50)

#A program to display employee information
def employee(fullname,age,position, maritalstatus):
    print(fullname,age,position,maritalstatus)
employee("Mark Sigei",54, "Human Resources Manger", "Married")
employee("Weldon Sang",36, "Registrar", "Single")
employee("Bii Clement",45, "ICT Officer", "Married")
employee("Frank Lampard",29, "Coach", "Divorced")


