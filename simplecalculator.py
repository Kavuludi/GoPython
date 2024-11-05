from itertools import repeat

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

print("Please select the operation:\n" 
"1. Add\n" 
"2. Subtract\n" 
"3. Multiply\n" 
"4. Divide\n"
"5. Exit\n")
select = int(input("Select operations form 1, 2, 3, 4, 5:"))


if select == 1:
    print(num1, "+", num2,"=", add(num1,num2))

elif select == 2:
    print(num1, "-",num2, "=",sub(num1,num2))

elif select == 3:
    print(num1, "*", num2,"=", mul(num1,num2))

elif select == 4:
    print(num1, "/", num2, "=",div(num1,num2))
elif select == 5:
    exit()
else:
    print("Invalid input")
