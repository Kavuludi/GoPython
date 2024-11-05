temperature=12

if temperature>25:
    print("The room is too hot")
else:
    print("The room is too cold")

#A python program that checks 3 numbers and returns the smallest.
num1=78
num2=120
num3=90

if num1<num2 and num1<num3:
    print(num1, "is the smallest number.")
elif num2<num1 and num2<num3:
    print(num2, "is the smallest number.")
else:
    print(num3, "is the smallest number.") 

#A python program to check 3 numbers and return the largest.
if num1>num2 and num1>num3:
    print(num1, "is the biggest number.")
elif num2>num1 and num2>num3:
    print(num2, "is the biggest number.")
else:
    print(num3, "is the biggest number.")